import math


def bin_ent(p):
   return -math.log(p,2)*p-math.log(1-p,2)*(1-p)
