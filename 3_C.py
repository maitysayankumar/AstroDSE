#Reg No:20209110002
#Problem 3(C) using Euler Method
import matplotlib.pyplot as pl
import numpy as np
w_m=0.3
w_r=5e-5
w_d=0.7

Ho=70/3.086e19
def f(a,t):  #a--x, t--y
    return 1/(Ho*((w_m/a)+(w_r/a**2)+w_d*a**2)**0.5)

a0=1e-10
t0=0
h=0.005
a=a0
b=1.00
n=int((b-a)/h)
A=np.linspace(a,b,n+1)
T=np.zeros(n+2)
T[0]=t0
for i in range(len(A)):
    T[i+1]=T[i]+h*f(A[i],T[i])

pl.plot(T[0:n+1],A)
pl.title('a(t) vs t for $\\Lambda$CDM (flat universe)')
pl.xlabel('t(S)')
pl.ylabel('a(t)')
pl.grid()
pl.show()

    