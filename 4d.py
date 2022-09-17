import numpy as np
import matplotlib.pyplot as pl
c=3e8  			#In meter
Ho=70*1000 		#In Megaparsec
DH=c/Ho
wm=0.3
wr=1e-5 
wd=0.7     
zu=5.0
zl=0.0
w1=-1/2
w2=-2/3
za=np.pi/2
z=np.linspace(zl,zu,10000)
def f(z,w):
	return DH/(wm*(1+z)**3+wr*(1+z)**4+wd*(1+z)**(3*(1+w)))**0.5
def a(z,w):
	return 1/((np.cos(z)**2)*(1+np.tan(z))*(wm*(1+np.tan(z))**3+wr*(1+np.tan(z))**4+wd*(1+np.tan(z))**(3*(1+w)))**0.5)

n=len(z)-1
z1=np.linspace(zl,za,n)
ha=(za-zl)/n
sum_1= (a(zl,w1)+a(za,w1))/2
sum_2= (a(zl,w2)+a(za,w2))/2
for i in range(1,n):
    sum_1 += a(z1[i],w1)
    sum_2 += a(z1[i],w2)
age1=ha*sum_1/Ho*3.086e22/3.154e16
age2=ha*sum_2/Ho*3.086e22/3.154e16
print('Age of the Universe is:',age1,'for',w1)
print('===================================')
print('Age of the Universe is:',age2,'for',w2)
h=(zu-zl)/n
Z=[]
dm1=[]
dm2=[]
ld1=np.zeros(n)
ad1=np.zeros(n)
ld2=np.zeros(n)
ad2=np.zeros(n)
idm1=0.0
idm2=0.0
x=0.0
for i in range(1,n+1):
  
    dm1.append(idm1) 
    dm2.append(idm2)   
    x=i*h
    Z.append(x)  
    sum1= (f(0,w1)+f(x,w1))/2
    sum2= (f(0,w2)+f(x,w2))/2
    x1=np.linspace(0.0,x,1000)
    n1=len(x1)-1
    h1=(x-zl)/n1
    for j in range(1,n1):
        sum1 += f(x1[j],w1)     
        sum2 += f(x1[j],w2)    
        idm1=h1*sum1
        idm2=h1*sum2
for i in range(n):
    ld1[i]=dm1[i]*(1+Z[i])
    ad1[i]=dm1[i]/(1+Z[i])
    ld2[i]=dm2[i]*(1+Z[i])
    ad2[i]=dm2[i]/(1+Z[i])
pl.plot(Z,dm1,label='distance(-1/2)')
pl.plot(Z,ld1,label='Luminosity(-1/2)')
pl.plot(Z,ad1,label='Angular(-1/2)')
pl.plot(Z,dm2,label='distance(-2/3)')
pl.plot(Z,ld2,label='Luminosity(-2/3)')
pl.plot(Z,ad2,label='Angular(-2/3)')
pl.legend()
pl.grid()
pl.show()

