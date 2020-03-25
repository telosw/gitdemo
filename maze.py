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
for row in range (0,num_rows):
    for col in range(0,num_cols):
        data=M[row,col]
        for i in range(10*row+2,10*row+8):
            image[i,range(10*col+2,10*col+8)]=3000
        if data[0]==1:
            image[range(10*row+2,10*row+8),10*col] = 3000
            image[range(10*row+2,10*row+8),10*col+1] =3000
        if data[2]==1:
            image[range(10*row+2,10*row+8),10*col+9] = 3000
            image[range(10*row+2,10*row+8),10*col+8] = 3000
        if data[1]==1:
            image[10*row,range(10*col+2,10*col+8)] = 3000
            image[10*row+1,range(10*col+2,10*col+8)] = 3000
        if data[3]==1:
            image[10*row+9,range(10*col+2,10*col+8)] = 3000
            image[10*row+8,range(10*col+2,10*col+8)] = 3000
image[range(4,6),5]=1000
image[5,range(4,6)]=1000
image[range(4,6),4]=1000
plt.imshow(image,cmap=cm.Pastel1_r)
plt.show()
for i in way:
    image[range(10*i[0]+4,10*i[0]+6),10*i[1]+5]=2000
    image[10*i[0]+5,range(10*i[1]+4,10*i[1]+6)]=2000
    image[range(10*i[0]+4,10*i[0]+6),10*i[1]+4]=2000
plt.imshow(image,cmap=cm.Pastel1_r)
plt.show()
