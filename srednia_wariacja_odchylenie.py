# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:27:54 2022

@author: Ania
"""
from math import sqrt
import numpy as np
macierz=[]
with open("australian.dat", "r", encoding="utf-8") as f:
    for line in f:
        macierz.append(list(map(lambda x:float(x),line.split())))
        

def mean(wektor:list):
    return sum(wektor)/len(wektor)

def mean_lekcja(wektor:list):
    dl=len(wektor)
    w2=np.ones(dl)
    
    return np.dot(wektor,w2)/dl

def mean_but_aus(data:[list]):
    lista=[]
    for numeracja in range (len(data[0])-1):
        suma=0
        for element in data:
            suma+=element[numeracja]
        lista.append(suma/len(data))
    return lista


lista=[2,3,4,5,9]
# print(mean_but_aus(macierz))
print(mean_lekcja(lista))
def wariacja_lekcja(data:[list]):
    dl=len(data)
    w2=np.ones(dl)
    temp=mean_lekcja(data)*w2
    odejm=data-temp
    wynik=np.dot(odejm,odejm)  /dl 
    return wynik
def odchyl_lekcja(data:[list]):
    war=wariacja_lekcja(data)
    return sqrt(war)
    

lista=[10,12,9,1,3,4.5,9.2]
print(wariacja_lekcja(lista),odchyl_lekcja(lista))

lista_tupli=[[2,1], [5,2],[7,3],[8,3]]
# 2/7 /14

def trans(macierz):
    m2=[]
    m3=[]
    m4=[]
    for i in macierz :
        m2.append(i[0])
        m3.append(i[1])
    m4.append(m2)
    m4.append(m3)
    return m4
# print(trans(lista_tupli))
def wyznacznik(macierz):
    wyzn=macierz[0][0]*macierz[1][1]-macierz[0][1]*macierz[1][0]
    if wyzn==0:
        return None
    else :
        return wyzn
    
def odwr_mac(macierz):
    l=[]
    l3=[]
    for i in range (len(macierz)):
        for j in range (len(macierz[i])):
            w=pow((-1),(i+j))*macierz[1-i][1-j]
            l.append(w)
    l1=l[:len(l)//2]
    l2=l[len(l)//2:]
    l3.append(l1)
    l3.append(l2)
  
    a=np.asarray(l3)
    a=np.asarray(trans(a))
    print(1/wyznacznik(macierz)*a)
    return 1/wyznacznik(macierz)*a
    

          
        

def macierzuj(lista_tup):
    lista_y=[]
    macierz=[]
    for tup in lista_tup:
        lista_y.append([tup[1]])
        macierz.append([1,tup[0]])
    xTx=(np.dot(trans(macierz),macierz))
    xTy=(np.dot(trans(macierz),lista_y))
    b=np.dot(odwr_mac(xTx),xTy)
    return b
    
print(macierzuj(lista_tupli))


# w formie pisemnej macierzy i rozłozyc 

    
    
# def wariancja(data:[list]):
#     lista=[]
#     lista_sr=mean_but_aus(data)
#     for num in range (len(data[0])-1):
#         suma=0
#         for element in data:
#             roznica=pow(element[num]-lista_sr[num],2)
#             suma+=roznica
#         lista.append(suma/(len(data)))
#     return lista
# def odchyl(data:[list]):
#     lista=[]
#     war=wariancja(data)
#     for i in range (len(war)):
#         lista.append(sqrt(war[i]))
#     return lista
    
# print(wariancja(macierz))
# print(odchyl(macierz))
