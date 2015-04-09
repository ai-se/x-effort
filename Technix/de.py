"""

# Place to store settings.

## Usual Header

"""
from __future__ import division,print_function
import  sys
sys.dont_write_bytecode = True
import random
from lib import *
from settings import *
from where2 import *
from Models.nasa93 import nasa93

def DE_settings(**d):
    return o(
       max     = 100,  # number of repeats
       # credit to @WeiFoo
       np      = 50,  # number of candidates
       f       = 0.4, # extrapolate amount
       cf      = 0.3,  # prob of cross-over
       lives   = 10
    ).update(**d)

def split_data(rows):
    random.shuffle(rows)
    size = len(rows)
            #Train          #Tune                   #Test
    return rows[:size//3], rows[size//3:-size//3], rows[-size//3:]


def trim(one, low, high):
  return max(low, min(one, high))

def between(low, high, prec=3):
  if isinstance(low, float):
    return round(random.uniform(low, high), prec)
  elif isinstance(low, bool):
    return bool(random.getrandbits(1))
  elif isinstance(low, int):
    return int(round(random.uniform(low, high)))
  return None


def MRE(model, inp, classifier, predictor):
  mre = N()
  for row in inp:
    desired = effort(model, row)
    pred = predictor(model, classifier, row)
    mre += abs(desired - pred)/desired
  return mre.cache.has().median


class Candidate(o):
  id = 0
  def __init__(i, de, cand= None):
    if cand:
      i.id = cand.id
      i.objectives = cand.objectives
      i.score = None
    else :
      i.id = Candidate.id =  Candidate.id+1
      i.generate(de.settings)
      i.evaluate(de)

  def generate(i, settings):
    obj = o()
    for index, key in enumerate(settings.params):
      obj.has()[key] = between(settings.min[index], settings.max[index])
    i.objectives = obj

  def evaluate(i, de):
    classifier = de.builder(de.model, i.objectives, de.train)
    i.score = MRE(de.model, de.tune, classifier, de.predictor)

  def __gt__(i, j):
    return i.score > j.score

class DE(o):
  "DE"
  id = 0
  def __init__(i, model, builder, predictor, settings):
    i.id = DE.id = DE.id+1
    i.model = model
    i.builder = builder
    i.predictor = predictor
    i.settings = settings
    i.train, i.tune, i.test = split_data(model._rows)
    i.config = DE_settings()
    i.frontier = i.build()

  """
  Build Frontier
  """
  def build(i):
    return [ Candidate(i) for _ in range(i.config.np)]

  def best(i):
    return sorted(i.frontier)[0]

  def run(i):
    lives = i.config.lives
    for _ in range(i.config.max):
      if lives == 0: break
      updated = i.update()
      print(updated)
      if not updated: lives -= 1
    return i.best()

  def update(i):
    nextGen = []
    oldBest = i.best()
    for point in i.frontier:
      mutated = i.mutate(point)
      if mutated > point:
        nextGen.append(mutated)
      else:
        nextGen.append(point)
    i.frontier= nextGen
    newBest = i.best()
    if newBest > oldBest:
      return True
    return False


  def mutate(i, point, prec=3):
    mutated = Candidate(i, point)
    two, three, four = i.threeMore(point)
    obj2, obj3, obj4 = two.objectives, three.objectives, four.objectives
    cf,f = i.config.cf, i.config.f
    for _, (key, low, high) in enumerate(zip(i.settings.params,i.settings.min, i.settings.max)):
      if random.random() > cf :
        if isinstance(low, float):
          extrapolated = trim(round(obj2[key] + f*(obj3[key] - obj4[key]), prec), low, high)
        elif isinstance(low, bool):
          extrapolated  = bool(random.getrandbits(1))
        elif isinstance(low, int):
          extrapolated =  trim(int(round(random.uniform(low, high))), low, high)
        mutated.objectives.has()[key] = extrapolated
    mutated.evaluate(i)
    return mutated

  def threeMore(i, one):
    seen = [one.id]
    def oneMore(seen):
      while True:
        point = random.choice(i.frontier)
        if point.id not in seen:
          seen += [point.id]
          return point
    return oneMore(seen), oneMore(seen), oneMore(seen)
