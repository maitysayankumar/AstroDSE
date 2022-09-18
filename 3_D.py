#Reg No:20209110002
#Problem 3(D) using Euler Method
import matplotlib.pyplot as pl
import numpy as np
Ho=70/3.086e19
wm=0.3
wr=5e-5
wk1=-0.3
wk2=-0.5
wk3=-0.7
def f(a,t,wk):  #a-->x, t-->y
    return 1/(Ho**2*(wm/a +wr/a**2 -wk))**0.5          

a0=1e-10 #Initial Conditions at t=0 a=0 (Big Bang)
t0=0
h=0.005
a=a0    #Lower limit of a(t)
b=1.00  #Upper limit of a(t)
n=int((b-a)/h)

A=np.linspace(a,b,n+1)
T1=np.zeros(n+2)
T2=np.zeros(n+2)
T3=np.zeros(n+2)
T1[0]=a0
T2[0]=a0
T3[0]=a0
for i in range(len(A)):
    T1[i+1]=round(T1[i]+h*f(A[i],T1[i],wk1),4)
    T2[i+1]=round(T2[i]+h*f(A[i],T1[i],wk2),4)
    T3[i+1]=round(T3[i]+h*f(A[i],T1[i],wk3),4)


pl.plot(T1[0:n+1],A,label='$\\Omega_k$ =-0.3')
pl.plot(T2[0:n+1],A,label='$\\Omega_k$ =-0.5')
pl.plot(T3[0:n+1],A,label='$\\Omega_k$ =-0.7')
pl.title('a(t) vs t(s) graph for open universe (no dark energy)')
pl.xlabel('t(S)')
pl.ylabel('a(t)')
pl.legend()
pl.grid()
pl.show()