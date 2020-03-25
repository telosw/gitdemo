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
def find_way(way):
    if no_repeat(way)[0]==1:
        return way
    else:
        m=max(no_repeat(way)[1],no_repeat(way)[2])
        n=min(no_repeat(way)[1],no_repeat(way)[2])
        del way[n:m]
        return find_way(way)
num_rows=int(input('请输入列数:'))
num_cols=int(input('请输入行数:'))
image=np.zeros((num_rows*10,num_cols*10),dtype=np.uint8)
M=np.zeros((num_rows,num_cols,5),dtype=np.uint8)
r,c=0,0
history=[(0,0)]
way=[]