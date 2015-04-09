from Technix.de import *

if __name__=="__main__":
  de = DE(nasa93(), launchWhere2, predictPEEKING, peekSettings())
  cand = Candidate(de)
  print(cand.score)