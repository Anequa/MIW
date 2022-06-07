

from wartosci_macierzy_wlasnych import wartosci_wlasne
import math
import numpy as np

def gauss (macierz):
    rozmiar=len(macierz)
    for i in range (rozmiar-1):
        dziel=macierz[i][i]
        for j in range (i,rozmiar):
            macierz[i][j]=macierz[i][j]/dziel
        for z in range (i+1,rozmiar):
            odejmij=macierz[z][i]
            for y in range(rozmiar):
                macierz[z][y]=macierz[z][y]-odejmij*macierz[i][y]
    for a in range (rozmiar-2,0,-1):
        for b in range (a-1,-1,-1):
            mnoz=macierz[b][a]
            wiersz=macierz[a]*mnoz
            macierz[b]-=wiersz
    return [-macierz[y][rozmiar-1] for y in range (rozmiar-1)]
            
        
        
    
# def przekatna(macierz):
#     przekatna=[]
#     for i in range(rozmiar(macierz)):
#         przekatna.append(macierz[i][i])
#     return przekatna
        
    
def macierz_zmieniona(macierz,wart_wlasna):
    macierz2=macierz.copy()
    rozmiar=len(macierz)
    for i in range (rozmiar):
        macierz2[i][i]=macierz2[i][i]-wart_wlasna
    return macierz2

# macierz=[[4.185,2,3,4,5],[2,5.185,3,4,5],[3,3,6.185,4,5],[4,4,4,7.185,5],[5,5,5,5,8.185]]
# macierz=np.array(macierz)
# g=gauss(macierz)
# print(g)
macierz=[[1.,2.,3.,4.,5.],[2.,2.,3.,4.,5.],[3.,3.,3.,4.,5.],[4.,4.,4.,4.,5.],[5.,5.,5.,5.,5.]]
macierz=np.array(macierz)
wynik=wartosci_wlasne(macierz)
for i in wynik:
    tmp=macierz_zmieniona(macierz,i)
    # print(gauss(tmp)+[1])
    


    
