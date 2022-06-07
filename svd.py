from math import sqrt
import numpy as np
from QA import macierzR, ortogonalizacja
from wartosci_macierzy_wlasnych import wartosci_wlasne
from gauss import  macierz_zmieniona,gauss

a=np.array([[1.,2., 0.],[2., 0., 2.]])
ata=np.dot(a.T,a)
aat=np.dot(a,a.T)
l=sorted(np.round(wartosci_wlasne(aat)),reverse=True)


u=[]
sigmy=[]
for i in l:
    tmp=macierz_zmieniona(aat,i)
    u.append((gauss(tmp)+[1.]))
    sigmy.append((sqrt(int(i))))
u=np.array(u)  
sigmy=np.array(sigmy)
# print(sigmy)
# print(u)
for ind,i in enumerate(u):
    b=(1/sqrt(np.dot(i.T,i)))
    u[ind]=i*b
# print(u)

tempv=[]
wart_wl_v=sorted(wartosci_wlasne(ata),reverse=True)
for i in wart_wl_v:
    tmp=macierz_zmieniona(ata,i)
    tempv.append((gauss(tmp)+[1.]))
tempv=np.array(tempv)  


def oblicz_v(a,u,sigma):
    v=[]
    for i in range(len(u)):
        si=(sigma[i])
        ui=u[i]
        print(si)
        v.append(np.dot(a.T,ui.T)*(1/si) )
    v.append(tempv[-1])
    return np.array(v)



print(oblicz_v(a,u,sigmy))


