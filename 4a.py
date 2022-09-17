import numpy as np
import matplotlib.pyplot as pl
c=3e8  #In meter
Ho=70*1000 #In Megaparsec
DH=c/Ho
wm=0.0
wr=1.0/3.0
zu=5.0
zl=0.0
z=np.linspace(zl,zu,10000)
def f(z,w):
	return 2*DH*(1-(1+z)**((-1-3*w)/2))/(1+3*w)

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
pl.xlabel('redshift(z)')
pl.ylabel('Distance(MPc)')
pl.grid()
pl.legend()
pl.show()
