# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:30:58 2022

@author: Ania
"""
import numpy as np
from math import sqrt

def ortogonalizacja(macierz):
   
    trans=macierz.T
    listaU=[trans[0]]
    listaE=[]
    for v in trans[1:]:
        sumaProj=0
        for u in listaU:
            proj=projekcja(u, v)
            sumaProj+=proj
        listaU.append(v-sumaProj)
    for u in listaU:
        listaE.append(dzielDlug(u))
    return np.around(np.array(listaE).T,6)


def macierzR(macierz):
    q=ortogonalizacja(macierz)
    return q.T.dot(macierz)

def sprawdz(macierz):
    q=ortogonalizacja(macierz)
    r=macierzR(macierz)
    return q.dot(r)
    
    
def dzielDlug(u):
    return u/sqrt(np.dot(u.T,u))

def projekcja(u,v):
    gora=v.dot(u)
    dol= u.dot(u)
    return (gora/dol)*u
    
# print(projekcja(np.array([1,1,0]), np.array([0,1,1])))
        
# macierz=np.array([[2,0,1],[0,1,1],[1,2,1]])
# print(ortogonalizacja(macierz))
# print(macierzR(macierz))
# print(np.around(sprawdz(macierz),0))
