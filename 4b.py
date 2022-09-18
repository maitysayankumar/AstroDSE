#Reg No:20209110002
#CRN:PHYS002
import numpy as np
import matplotlib.pyplot as pl
c=3e8  			#In meter/s
Ho=70*1000 		#In Megaparsec
DH=c/Ho
wm=0.3
wr=1e-5 
wd=0.7     
zu=5.0
zl=0.0
za=np.pi/2
z=np.linspace(zl,zu,10000)
def f(z):
	return DH/(wm*(1+z)**3+wr*(1+z)**4+wd)**0.5
def a(z):
	return 1/((np.cos(z)**2)*(1+np.tan(z))*(wm*(1+np.tan(z))**3+wr*(1+np.tan(z))**4+wd)**0.5)

n=len(z)-1
z1=np.linspace(zl,za,n)
ha=(za-zl)/n
sum= (a(zl)+a(za))/2
for i in range(1,n):
    sum += a(z1[i])
age=ha*sum/Ho*3.086e22/3.154e16  #Seconds to Billion Years Conversion
print('Age of the Universe is:',age)

n=len(z)-1
h=(zu-zl)/n
Z=[]
dm=[]
ld=np.zeros(n)
ad=np.zeros(n)
idm=0.0
x=0.0
for i in range(1,n+1):
  
    dm.append(idm)   
    x=i*h
    Z.append(x)  
    sum1= (f(0)+f(x))/2
    x1=np.linspace(0.0,x,1000)
    n1=len(x1)-1
    h1=(x-zl)/n1
    for j in range(1,n1):         #Composite trapezoidal rule
        sum1 += f(x1[j])        
        idm=h1*sum1
        
for i in range(n):
    ld[i]=dm[i]*(1+Z[i])
    ad[i]=dm[i]/(1+Z[i])
pl.plot(Z,dm,label='Distance')
pl.plot(Z,ld,label='Luminosity Distance')
pl.plot(Z,ad,label='Angular Diameter Distance')
pl.xlabel('Redshift(z)')
pl.ylabel('Distance(Mpc)')
pl.title('Distance vs Redshift Plot for $\\Lambda CDM$')
pl.legend()
pl.grid()
pl.show()

