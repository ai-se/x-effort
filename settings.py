"""

# Place to store settings.

## Usual Header

"""
import  sys
sys.dont_write_bytecode = True
"""

## Anonymous Containers

"""
class o:
  def __init__(i,**d): i.has().update(**d)
  def has(i): return i.__dict__
  def update(i,**d) : i.has().update(d); return i
  def __repr__(i)   :
    show=[':%s %s' % (k,i.has()[k])
      for k in sorted(i.has().keys() )
      if k[0] is not "#"]
    txt = ' '.join(show)
    if len(txt) > 60:
      show=map(lambda x: '\t'+x+'\n',show)
    return '{'+' '.join(show)+'}'
  def __getitem__(i, item):
    return i.has().get(item)


class E:
  def __init__(i,txt):
    i.txt   = txt
    i._f    = None
  def __call__(i,*lst,**d):
    return i.f()(*lst,**d)
  def f(i):

    if not i._f: i._f=globals()[i.txt]
    return i._f
  def __repr__(i):
    return i.txt+'()'

def defaults(**d):
  return o(_logo="""
            |    |    |
            |    |    |
            |    |    |
            \    |    /
             |   |   |
             |   |   |
             |   |   |
             \   |   /
              |  |  |
              |  |  |
              |  |  |
              |  |  |
            """,
      what=o(
            b4      = '|.. ', # indent string
            verbose = False,  # show trace info?
            goal    = lambda m,x : scores(m,x)
      ),
      seed    = 1,
      cache   = o(size=128)
  ).update(**d)

def configs(**d):
  return o(
    minSize   = 8,      # min leaf size
    depthMin  = 2,      # no pruning till this depth
    depthMax  = 10,     # max tree depth
    wriggle   = 0.2,    # min difference of 'better'
    prune     = True,   # If pruning should be performed
  ).update(**d)


def peekSettings():
    return o(
        params   = ["minSize", "depthMin", "depthMax", "wriggle", "prune", "neighbors"],
        defaults = [8,         2,          10,          0.2,       True,     2],
        max      = [30,        6,          30,          0.5,       True,     6],
        min      = [2,         2,          4,          0.01,       False,    2]
    )

The=None
