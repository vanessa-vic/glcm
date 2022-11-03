# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FJXvcZLohKVHR_SEgPlG-IEwRZqIIB4d
"""

import numpy as np

I=[[2,2,3,4],[3,1,5,3],[2,3,4,6],[2,3,2,4]]
#%OFFSET AND DIRECTION
Displacementx = -1;  
Displacementy = 0;  
As=[]
s=np.reshape(I,(16,1))
for i in range (len(I[:])):
  for j in range (len(I[:])):
    A = (I[i][j]-min(s[:]))+1;
    As.append(A)

NumQuantLevels = max(As)
x = np.zeros((NumQuantLevels[0],NumQuantLevels[0]))
glcm = x

print(glcm)

size_img=3
if ( Displacementx < 0 ) :
    sx=abs(Displacementx)+1;
    ex=size_img;
else:
    sx=1;
    ex=size_img-Displacementx;

if ( Displacementy < 0 ) :
    sy=abs(Displacementy)+1;
    ey=size_img
else:
    sy=1;
    ey =size_img-Displacementy;

As=np.reshape(As,(4,4))

print(As)
print(sx,ex,sy,ey)

c=(As[2+(1*Displacementx),3+(1*Displacementy)])
g=(As[2,3])
print(g,c)

for i in range(sx,ex,1):
    for j in range(sy,ey,1):
        c=(As[i+(1*Displacementx),j+(1*Displacementy)])
        g=(As[i,j])
        glcm[g][c]=((glcm[g][c])+1)
    
print (glcm)

gl=np.reshape(glcm,(NumQuantLevels[0]**2,1))

GLCMProb=[]
for i in range (NumQuantLevels[0]**2):
  GLCM= gl[i]/sum(gl)
  GLCMProb.append(GLCM)





import math
jj,ii = np.meshgrid(1,size(glcm,1),1:size(glcm,2));
ij=ii-jj;


for i in range (NumQuantLevels[0]**2):
  Con = sum(sum(GLCMProb[i]*gl[i]**2))
  Hom = sum(sum(GLCMProb[i]/(1+gl[i]**2)))
  Asm = sum(sum(GLCMProb[i]**2))
  Meanx = sum(sum(GLCMProb[i]*ii)); 
  Meany = sum(sum(GLCMProb[i]*jj));        
  Energy = math.sqrt(Asm)

  GLCMMean = (Meanx+Meany)/2;
  Varx = sum(sum(GLCMProb[i]*(ii-Meanx).**2));
  Vary = sum(sum(GLCMProb[i]*(jj-Meany).**2));
  GLCMVar = (Varx+Vary)/2;
  GLCMCorrelation = sum(sum(GLCMProb.*(ii-Meanx).*(jj-Meany)/sqrt(Varx*Vary))); %Correlation

ValueGLCM=[Con,Hom,Asm,Energy,GLCMCorrelation];



