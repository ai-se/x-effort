"""
# The coc2010 Data Set
Mystery Dataset - 2

Standard header:

"""
from __future__ import division,print_function
import  sys
sys.dont_write_bytecode = True
from  lib import *
"""

Data:

"""
def Mystery2(weighFeature = False,
            split = "median"):
  vl=1;l=2;n=3;h=4;vh=5;xh=6;_=0
  return data(indep= [ 
      'Prec','Flex','Resl','Team','Pmat','rely','data','ruse','docu','cplx','time', #0..10
      'stor','pvol','acap','pcap','aexp','plex','ltex','pcon','tool','site','sced', #11..22
      'size'], #23
    less = ['pm'],
    _rows=[
#0  1  2  3  4  5  6  7 8   9 10 11 12 13 14 15 16 17 18 19 20 21 22    23
[4, 4, 4, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 315, 112],
[3, 2, 3, 2, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1912.9, 526.5],
[5, 3, 4, 2, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 296.1, 75.6],
[4, 3, 4, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 538.65, 267],
[2, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1167.1, 304.4],
[2, 2, 3, 2, 4, 3, 4, 3, 3, 5, 4, 4, 3, 4, 3, 3, 2, 2, 4, 4, 3, 3, 151.5, 1944],
[4, 2, 3, 4, 4, 3, 4, 3, 4, 5, 4, 4, 3, 4, 3, 4, 3, 3, 4, 4, 3, 3, 37.18, 222],
[4, 4, 3, 4, 2, 3, 3, 3, 2, 5, 4, 3, 3, 5, 5, 5, 3, 1, 5, 3, 3, 3, 16, 34],
[4, 3, 3, 4, 2, 3, 3, 3, 2, 5, 4, 3, 3, 4, 4, 4, 4, 3, 4, 3, 3, 3, 19.03, 53],
[4, 2, 2, 3, 2, 4, 4, 3, 3, 5, 4, 4, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 26.94, 284],
[4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 92.2, 394],
[4, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 4, 3, 4, 4, 3, 3, 236.58, 573],
[4, 2, 3, 3, 4, 4, 3, 3, 4, 5, 4, 4, 2, 4, 4, 4, 4, 4, 4, 3, 2, 3, 45.29, 153],
[3, 1, 2, 2, 3, 5, 5, 2, 3, 4, 5, 4, 5, 4, 4, 5, 4, 3, 3, 3, 5, 3, 146.67, 542],
[2, 1, 1, 4, 2, 4, 5, 2, 2, 4, 5, 4, 5, 4, 4, 5, 4, 4, 3, 3, 3, 3, 209.62, 529],
[2, 1, 2, 3, 2, 4, 5, 2, 2, 4, 4, 4, 5, 4, 4, 5, 3, 4, 3, 2, 5, 2, 280.91, 973],
[3, 1, 2, 4, 5, 4, 5, 3, 2, 4, 3, 3, 3, 4, 4, 5, 3, 3, 3, 3, 5, 2, 168, 399],
[2, 3, 2, 3, 2, 3, 5, 2, 1, 4, 3, 3, 5, 4, 4, 5, 4, 4, 3, 3, 5, 2, 364.49, 684],
[2, 3, 2, 3, 2, 3, 5, 2, 1, 4, 3, 3, 5, 4, 4, 5, 4, 4, 3, 3, 5, 3, 328.65, 560],
[1, 2, 3, 3, 4, 4, 4, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 274.3, 619],
[2, 2, 3, 1, 4, 4, 5, 2, 3, 4, 3, 3, 4, 4, 4, 3, 4, 4, 3, 4, 5, 1, 736.49, 2320],
[4, 4, 3, 5, 3, 4, 3, 4, 2, 4, 4, 3, 2, 3, 3, 2, 2, 2, 3, 4, 2, 2, 106.76, 376.3],
[4, 4, 3, 5, 3, 4, 5, 4, 4, 5, 4, 4, 4, 3, 3, 2, 3, 3, 2, 2, 2, 2, 5.38, 112.2],
[4, 4, 3, 5, 3, 4, 5, 4, 4, 5, 4, 4, 4, 3, 3, 2, 3, 3, 2, 2, 2, 2, 5.38, 86.7],
[4, 4, 3, 5, 3, 3, 3, 4, 3, 3, 3, 3, 2, 4, 4, 5, 5, 4, 5, 4, 3, 3, 55.36, 72.4],
[4, 4, 3, 5, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 50.95, 87.7],
[4, 4, 3, 5, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 69.69, 88.7],
[4, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 14.55, 7.1],
[4, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 12.78, 11.2],
[4, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 4.23, 12.2],
[4, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 6.28, 10.2],
[3, 1, 3, 3, 5, 4, 5, 3, 3, 4, 3, 3, 4, 3, 4, 5, 4, 4, 3, 3, 3, 3, 88.1, 239],
[3, 2, 3, 3, 3, 4, 5, 3, 3, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 3, 5, 3, 155.4, 203],
[3, 2, 3, 3, 4, 4, 5, 3, 3, 4, 3, 3, 3, 4, 4, 5, 4, 4, 5, 3, 4, 3, 88.4, 106],
[4, 1, 2, 2, 4, 4, 5, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 1, 593.7, 2673],
[3, 2, 2, 3, 4, 4, 4, 2, 2, 4, 3, 3, 4, 4, 4, 4, 4, 4, 5, 3, 4, 1, 95.7, 161.76],
[3, 2, 3, 3, 4, 4, 5, 2, 2, 4, 4, 3, 3, 3, 4, 4, 4, 3, 4, 3, 4, 1, 92, 372.75],
[3, 3, 2, 3, 4, 4, 4, 2, 2, 4, 4, 3, 4, 4, 3, 2, 4, 3, 2, 3, 4, 1, 43.69, 118.6],
[3, 3, 2, 3, 4, 4, 4, 2, 1, 4, 4, 3, 4, 4, 3, 2, 4, 3, 2, 3, 4, 1, 43.69, 204.6],
[3, 2, 2, 3, 3, 4, 5, 2, 2, 4, 3, 3, 4, 4, 4, 5, 4, 4, 5, 3, 4, 3, 137, 196.78],
[4, 1, 4, 3, 4, 4, 5, 2, 3, 4, 3, 3, 3, 4, 4, 5, 4, 4, 4, 3, 5, 3, 55.4, 48.22],
[4, 2, 4, 3, 4, 4, 5, 3, 2, 4, 3, 4, 3, 3, 4, 5, 4, 4, 4, 3, 5, 3, 642.82, 1585],
[1, 4, 3, 2, 2, 4, 3, 3, 2, 4, 4, 3, 2, 3, 3, 2, 2, 2, 3, 4, 2, 2, 107.33, 376.03],
[5, 4, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 4, 4, 5, 5, 4, 5, 4, 3, 3, 55.65, 75.1],
[5, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 60.28, 87.85],
[5, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 82.45, 88.3],
[5, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 37.16, 7.24],
[5, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 32.65, 11.22],
[4, 4, 3, 5, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 13.44, 19.4],
[4, 4, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 2, 4, 4, 5, 5, 4, 5, 3, 3, 3, 12.97, 14.3],
[4, 4, 3, 5, 3, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 2, 4, 3, 6.47, 12.2],
[4, 4, 3, 5, 3, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 2, 4, 2, 27.6, 61.2],
[4, 4, 3, 5, 3, 4, 4, 3, 4, 4, 3, 3, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2.77, 19.4],
[4, 4, 3, 5, 3, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 2, 2, 3, 2, 7.07, 67.3],
[4, 4, 3, 5, 3, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 2, 4, 3, 5.7, 20.4],
[4, 4, 3, 5, 3, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 2, 2, 4, 3, 1.69, 21.4],
[1, 3, 3, 4, 3, 4, 3, 2, 4, 6, 6, 6, 3, 4, 4, 1, 4, 3, 3, 2, 6, 3, 25.78, 446.34],
[2, 1, 3, 3, 3, 4, 3, 3, 4, 5, 6, 3, 2, 3, 3, 5, 2, 4, 1, 1, 6, 3, 43.19, 860.64],
[4, 3, 2, 5, 3, 3, 3, 2, 3, 5, 3, 3, 2, 4, 4, 4, 1, 4, 3, 1, 2, 3, 90.58, 234.7],
[4, 5, 3, 5, 3, 3, 3, 2, 3, 4, 6, 3, 2, 5, 5, 5, 4, 3, 5, 2, 6, 3, 56.82, 230.48],
[2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 3, 2, 5, 4, 4, 1, 2, 4, 2, 6, 3, 41.65, 127.1],
[3, 3, 3, 5, 3, 3, 3, 2, 3, 4, 4, 4, 2, 5, 5, 5, 1, 5, 4, 3, 6, 3, 133, 285.6],
[3, 5, 3, 3, 3, 4, 3, 2, 3, 3, 5, 3, 2, 2, 4, 4, 4, 5, 2, 2, 6, 3, 16, 72],
[3, 3, 4, 3, 3, 5, 3, 4, 3, 4, 3, 3, 2, 3, 4, 3, 1, 4, 3, 5, 2, 3, 74.12, 314],
[5, 2, 5, 5, 5, 3, 3, 3, 3, 4, 3, 4, 3, 5, 3, 3, 2, 2, 2, 5, 5, 2, 168.92, 899.7],
[5, 2, 5, 5, 5, 3, 2, 3, 3, 4, 3, 3, 3, 5, 3, 4, 2, 2, 2, 5, 5, 2, 46.44, 171.2],
[2, 1, 5, 5, 5, 3, 2, 4, 3, 4, 4, 3, 2, 3, 3, 3, 3, 3, 2, 4, 5, 1, 171.05, 812.1],
[2, 3, 5, 5, 3, 4, 2, 4, 3, 4, 6, 6, 4, 1, 3, 3, 2, 3, 3, 4, 5, 3, 89.21, 212.6],
[3, 1, 3, 3, 5, 4, 5, 3, 3, 4, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 175.3, 457],
[5, 4, 3, 5, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 10.8, 12.24],
[5, 4, 3, 5, 3, 4, 4, 3, 4, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 3, 3, 3, 16.03, 10.2],
[3, 3, 3, 3, 1, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 4, 3, 7.74, 11.84],
[3, 3, 3, 3, 1, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 2, 4, 2, 33.02, 61.09],
[5, 3, 3, 3, 1, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 2, 2, 3, 2, 5.17, 66.84],
[3, 3, 3, 3, 1, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 2, 4, 3, 6.81, 20.52],
[3, 3, 3, 3, 1, 4, 4, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 2, 2, 4, 3, 2.02, 21.11],
[3, 3, 3, 3, 3, 4, 3, 4, 3, 3, 5, 4, 3, 5, 5, 5, 1, 1, 2, 3, 5, 3, 52.86, 244.5],
[3, 3, 3, 3, 3, 4, 3, 4, 3, 2, 3, 4, 2, 5, 4, 2, 2, 2, 5, 3, 3, 3, 6.65, 14.3],
[3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 5, 5, 1, 3, 4, 1, 3, 4, 3, 8.94, 29.7],
[3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 4, 2, 3, 3, 5, 3, 3, 2, 2, 5, 3, 25.02, 97],
[3, 3, 3, 3, 3, 2, 3, 2, 2, 2, 4, 4, 2, 4, 3, 1, 3, 2, 2, 3, 5, 3, 72.97, 301.9],
[3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 5, 4, 3, 5, 5, 5, 1, 1, 2, 3, 3, 3, 8.87, 25.6],
[4, 3, 3, 3, 4, 3, 3, 2, 3, 3, 3, 3, 3, 4, 4, 5, 4, 4, 3, 3, 5, 1, 218.73, 850],
[2, 4, 2, 2, 5, 3, 2, 2, 3, 6, 3, 3, 3, 5, 4, 5, 5, 5, 3, 4, 1, 2, 410.29, 1393],
[4, 4, 3, 4, 4, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 4, 6, 3, 268.43, 471],
[3, 2, 3, 3, 5, 3, 4, 4, 3, 3, 4, 3, 3, 3, 3, 4, 4, 4, 5, 3, 6, 3, 34.96, 126],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 5, 5, 3, 4, 4, 5, 1, 5, 3, 5.34, 3.5],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 5, 5, 3, 4, 4, 5, 1, 4, 3, 6.15, 4.5],
[3, 3, 3, 3, 3, 2, 4, 3, 4, 2, 3, 3, 2, 4, 5, 2, 2, 2, 3, 3, 4, 3, 5.83, 13.82],
[3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 3, 3, 4, 4, 1, 2, 2, 5, 3, 6, 3, 18.66, 13.82],
[3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 1, 4, 6, 3, 11.71, 9.21],
[3, 3, 3, 3, 3, 2, 4, 3, 3, 2, 3, 3, 2, 4, 4, 4, 5, 4, 4, 4, 5, 3, 19.24, 14.74],
[3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 1, 4, 6, 3, 15, 10.13],
[3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 4, 4, 3, 3, 3, 1, 4, 6, 3, 11.55, 38.68],
[3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 4, 4, 3, 2, 4, 3, 3, 3, 3, 15.95, 25.79]
    ],
    _tunings =[[
    #         vlow  low   nom   high  vhigh xhigh
    #scale factors:
    'Prec',   6.20, 4.96, 3.72, 2.48, 1.24, _ ],[
    'Flex',   5.07, 4.05, 3.04, 2.03, 1.01, _ ],[
    'Resl',   7.07, 5.65, 4.24, 2.83, 1.41, _ ],[
    'Pmat',   7.80, 6.24, 4.68, 3.12, 1.56, _ ],[
    'Team',   5.48, 4.38, 3.29, 2.19, 1.01, _ ]],
    weighFeature = weighFeature,
    _split = split
            
    )
"""

Demo code:

"""
def _coc2010(): print(coc2010())