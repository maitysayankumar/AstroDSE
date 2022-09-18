#Reg No:20209110002
#Problem 3(B) using Euler Method
import matplotlib.pyplot as pl
import numpy as np
w_m=1.0
Ho=70/3.086e19
def f(a,t):  #a--x, t--y
    return a**0.5/(Ho*w_m**0.5)
def g(a):              #Analytically solved solution
    return 2*a**1.5/(3*Ho*w_m**0.5)
a0=0   #Initial Conditions
t0=0
h=0.005
a=0.00    #Lower limit of a(t)
b=1.00    #Upper limit of a(t)
n=int((b-a)/h)

A=np.linspace(a,b,n+1)
T=np.zeros(n+2)
T[0]=t0
for i in range(len(A)):
    T[i+1]=round(T[i]+h*f(A[i],T[i]),4)

Ta=g(A[0:n+1])
pl.plot(T[0:n+1],A,label='Numerical')
pl.plot(Ta,A,'.',label='Analytical')
pl.title('a(t) vs t for matter only flat universe')
pl.xlabel('t(S)')
pl.ylabel('a(t)')
pl.legend()
pl.grid()
pl.show()

    