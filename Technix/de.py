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
       np      = 30,  # number of candidates
       f       = 0.4, # extrapolate amount
       cf      = 0.3,  # prob of cross-over
       lives   = 5
    ).update(**d)

def split_data(rows):
    random.shuffle(rows)
    size = len(rows)
            #Train          #Tune                   #Test
    return rows[:size//3], rows[size//3:-size//3], rows[-size//3:]


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
  def __init__(i, de):
    i.id = Candidate.id =  Candidate.id+1
    i.objectives, i.score = None, None
    i.generate(de.settings)
    i.evaluate(de)

  def generate(i, settings):
    obj = o()
    for index, key in enumerate(settings.params):
      obj.__dict__[key] = between(settings.min[index], settings.max[index])
    i.objectives = obj

  def evaluate(i, de):
    classifier = de.builder(de.model, i.objectives, de.train)
    i.score = MRE(de.model, de.tune, classifier, de.predictor)

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
    return [ Candidate(i) for _ in i.config.np]

  def extrapolate(i):
    #TODO extrapolate
    pass

  def run(i):
    for _ in range(i.config.max):
      # TODO
      pass


