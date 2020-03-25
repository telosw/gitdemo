import numpy as np
import random
from matplotlib import pyplot as plt
import matplotlib.cm as cm
def no_repeat(ls):
    d=0
    for i in range(len(ls)):
        for j in range(len(ls)):
            if j!=i and ls[i]==ls[j]:
                d=1
                return (0,i,j)
    if d==0:
        return (1,0,0)