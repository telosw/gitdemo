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
while history!=[]:
    M[r,c,4]=1
    choices=[]
    if c>0 and M[r,c-1,4]==0:
        choices.append('Le')
    if r>0 and M[r-1,c,4]==0:
        choices.append('Up')
    if c<num_cols-1 and M[r,c+1,4]==0:
        choices.append('Ri')
    if r<num_rows-1 and M[r+1,c,4]==0:
        choices.append('Do')
    if len(choices)!=0:
        history.append([r,c])
        way.append([r,c])
        direction=random.choice(choices)
        if direction=='Le':
            M[r,c,0]=1
            r,c=r,c-1
            M[r,c,2]=1
        if direction=='Up':
            M[r,c,1]=1
            r,c=r-1,c
            M[r,c,3]=1
        if direction=='Ri':
            M[r,c,2]=1
            r,c=r,c+1
            M[r,c,0]=1
        if direction=='Do':
            M[r,c,3]=1
            r,c=r+1,c
            M[r,c,1]=1
    else:
        way.append([r,c])
        r,c=history.pop()
M[0,0,0]=1
M[num_rows-1,num_cols-1,2]=1
for i in range(len(way)):
    if way[i] == [num_rows-1,num_cols-1]:
        way=way[:i+1]
        break
way=find_way(way)
