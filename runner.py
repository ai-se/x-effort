from Technix.de import *

if __name__=="__main__":
  # de = DE(nasa93(), launchWhere2, predictPEEKING, peekSettings())
  # cand = Candidate(de)
  # print(cand.score)
  set = peekSettings()
  print(set.has().keys())
  # for i, (key, min, max) in enumerate(zip(set.params,set.max, set.min)):
  #   print(i, key, min , max)