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
z=np.linspace(zl,zu,1000)
def f(z):
	return DH/(wm*(1+z)**3+wr*(1+z)**4+wd)**0.5


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
    for j in range(1,n1):
        sum1 += f(x1[j])
        
        idm=h1*sum1
        
for i in range(n):
    ld[i]=dm[i]*(1+Z[i])
    ad[i]=dm[i]/(1+Z[i])
pl.plot(Z,dm,label='distance')
pl.plot(Z,ld,label='Luminosity')
pl.plot(Z,ad,label='Angular')
pl.legend()
pl.grid()
pl.show()

print(ld[500])






#pl.plot(z,dm,label='Distance(Matter Only)')
#pl.plot(z,ldm,label='Luminosity Distance(Matter Only)')
#pl.plot(z,adm,label='Angular Diameter Distance(Matter Only)')
#pl.plot(z,dr,label='Distance(Radiation Only)')
#pl.plot(z,ldr,label='Luminosity Distance(Radiation Only)')
#pl.plot(z,adr,label='Angular Diameter Distance(Radiation Only)')
#pl.xlabel('redshift(z)')
#pl.ylabel('Distance(MPc)')
#pl.grid()
#pl.legend()
#pl.show()
