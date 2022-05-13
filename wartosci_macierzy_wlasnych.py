from QA import macierzR, ortogonalizacja
import math
import numpy as np

def wartosci_wlasne(macierz):
    przekontna=[]
    # Ak=np.dot(ortogonalizacja(macierz),macierzR(macierz))
    ak=macierz
    while True:
        aknext=np.dot(macierzR(ak),ortogonalizacja(ak))
        
        if(czyTrojkatnaGorna(aknext)):
            for i in range(rozmiar(macierz)):
                przekontna.append(aknext[i][i])
            return przekontna
        ak=aknext
        

        
def czyTrojkatnaGorna(macierz):
    for i in range(1,rozmiar(macierz)):
        for a in range(i):
            if(macierz[i][a])>0.0001:
                return False
    return True

def rozmiar(macierz):
    return len(macierz[0])
    

m=np.array([[1, 1, 2],[0, 0, 1],[4, 1, 1]])
print(wartosci_wlasne(m))
print(np.linalg.eigvals([[1, 1, 2],[0, 0, 1],[4, 1, 1]]))