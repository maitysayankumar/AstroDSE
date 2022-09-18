#Reg No:20209110002
#Problem 3(E) using Euler Method
import matplotlib.pyplot as pl
import numpy as np
Ho=70/3.086e19  #Hubble's Constant
w1=-2/3
w2=-1/2
wr=5e-5
wm=0.3
wd=0.7
def f(a,t,w):  #a-->x, t-->y
    return 1/(Ho**2*(wm/a +wr/a**2 + wd/a**(1+3*w)))**0.5   

a0=1e-10 #Initial Conditions at t=0 a=0 (Big Bang)
t0=0
h=0.005
a=a0    #Lower limit of a(t)
b=1.00  #Upper limit of a(t)
n=int((b-a)/h)

A=np.linspace(a,b,n+1)
T1=np.zeros(n+2)
T2=np.zeros(n+2)

T1[0]=0
T2[0]=0

for i in range(len(A)):
    T1[i+1]=T1[i]+h*f(A[i],T1[i],w1)
    T2[i+1]=T2[i]+h*f(A[i],T1[i],w2)



pl.plot(T1[0:n+1],A,label='$\\omega$''$=-\\frac{2}{3}$')
pl.plot(T2[0:n+1],A,label='$\\omega$''$=-\\frac{1}{2}$')

pl.title('a(t) vs t for $\\omega$ CDM (flat universe)')
pl.xlabel('t(S)')
pl.ylabel('a(t)')
pl.legend()
pl.grid()
pl.show()