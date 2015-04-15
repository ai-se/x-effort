from Technix.de import *
from Technix.TEAK import *
from Technix.CART import *
from Technix.sk import rdivDemo

MODEL = nasa93

def PEEKING_DE(model=MODEL, inp=None):
  mdl = model()
  if inp is None:
    inp = split_data(mdl._rows)
  train, tune, test = inp
  de = DE(model(), launchWhere2, predictPEEKING, peekSettings(), inp)
  best = de.run()
  #Tuned
  classifier = de.builder(de.model, best.objectives, train)
  mre = MRE(de.model, test, classifier, de.predictor)
  tuned = mre.cache.has().median
  #Untuned
  classifier = de.builder(de.model, settings=None, rows=train)
  mre = MRE(de.model, test, classifier, de.predictor)
  untuned = mre.cache.has().median
  return tuned, untuned

def TEAK_DE(model=MODEL, inp=None):
  mdl = model()
  if inp is None:
    inp = split_data(mdl._rows)
  train, tune, test = inp
  de = DE(model(), launchTeak, predictTeak, teakSettings(), inp)
  best = de.run()
  #Tuned
  classifier = de.builder(de.model, best.objectives, train)
  mre = MRE(de.model, test, classifier, de.predictor)
  tuned = mre.cache.has().median
  #Untuned
  classifier = de.builder(de.model, settings=None, rows=train)
  mre = MRE(de.model, test, classifier, de.predictor)
  untuned = mre.cache.has().median
  return tuned, untuned

def CART_DE(model=MODEL, inp=None):
  mdl=model()
  if inp is None:
    inp = split_data(mdl._rows)
  train, tune, test = inp
  de = DE(model(), launchTeak, predictTeak, teakSettings(), inp)
  best = de.run()
  #Tuned
  classifier = de.builder(de.model, best.objectives, train)
  mre = MRE(de.model, test, classifier, de.predictor)
  tuned = mre.cache.has().median
  #Untuned
  classifier = de.builder(de.model, settings=None, rows=train)
  mre = MRE(de.model, test, classifier, de.predictor)
  untuned = mre.cache.has().median
  return tuned, untuned

def _run(model=MODEL, cross_val=21):
  random.seed(1)
  errors = {
    "Peek" : N(),
    "t_Peek" : N(),
    "TEAK" : N(),
    "t_TEAK" : N(),
    "CART" : N(),
    "t_CART"  : N()
  }
  all_rows = model()._rows
  for _ in range(cross_val):
    print(_)
    inp = split_data(all_rows)
    t_err, err = TEAK_DE(model, inp)
    errors["TEAK"] += err; errors["t_TEAK"] += t_err
    t_err, err = PEEKING_DE(model, inp)
    errors["Peek"] += err; errors["t_Peek"] += t_err
    t_err, err = CART_DE(model, inp)
    errors["CART"] += err; errors["t_CART"] += t_err
  print("Peek", errors["Peek"].cache.all)
  print("t_Peek", errors["t_Peek"].cache.all)
  print("TEAK", errors["TEAK"].cache.all)
  print("t_TEAK", errors["t_TEAK"].cache.all)
  print("CART", errors["CART"].cache.all)
  print("t_CART", errors["t_CART"].cache.all)
  skData=[]
  for key, n in errors.items():
    skData.append([key]+n.cache.all)
  rdivDemo(skData,"cliffs")

if __name__=="__main__":
  _run(nasa93)