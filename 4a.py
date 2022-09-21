import numpy as np #sayan
import matplotlib.pyplot as pl
c=3e8  #In meter/s
Ho=70*1000 #In Megaparsec
DH=c/Ho
wm=0.0
wr=1.0/3.0
zu=5.0
zl=0.0
za=np.pi/2
z=np.linspace(zl,zu,10000)
def f(z,w):
	return 2*DH*(1-(1+z)**((-1-3*w)/2))/(1+3*w)

def a(z,w):
	return 1/(np.cos(z)**2*((1+np.tan(z))**(3*w/2+5/2)))

n=len(z)-1
z1=np.linspace(zl,za,n)
ha=(za-zl)/n
sum1= (a(zl,wm)+a(za,wm))/2
sum2= (a(zl,wr)+a(za,wr))/2
for i in range(1,n):              #Composite trapezoidal rule
    sum1 += a(z1[i],wm)
    sum2 += a(z1[i],wr)
age1=ha*sum1/Ho*3.086e22/3.154e16  #Seconds to Billion Years Conversion
age2=ha*sum2/Ho*3.086e22/3.154e16
print('Age of the matter only Universe is:',age1,'billion years.')
print('Age of the radiation only Universe is:',age2,'billion years.')

dm=f(z,wm)      #All distances are in Megaparsec unit
ldm=dm*(1+z)
adm=dm/(1+z)
dr=f(z,wr)
ldr=dr*(1+z)
adr=dr/(1+z)
pl.plot(z,dm,label='Distance(Matter Only)')
pl.plot(z,ldm,label='Luminosity Distance(Matter Only)')
pl.plot(z,adm,label='Angular Diameter Distance(Matter Only)')
pl.plot(z,dr,label='Distance(Radiation Only)')
pl.plot(z,ldr,label='Luminosity Distance(Radiation Only)')
pl.plot(z,adr,label='Angular Diameter Distance(Radiation Only)')
pl.xlabel('Redshift(z)')
pl.ylabel('Distance(Mpc)')
pl.title('Distance vs Redshift Plot (Single Component Universe)')
pl.grid()
pl.legend()
pl.show()

