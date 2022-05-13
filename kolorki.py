# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:04:45 2022

@author: Ania
"""
import random
from math import sqrt

def metryka_euplidesowa(a,b):
    c=0
    leng=max(len(a),len(b))-1
    for i in range (leng):
            el=pow(a[i]-b[i],2)
            c+=el
    return sqrt(c)

def readfile(name):
    matrix = list()
    with open(name, "r") as f:
        for line in f.readlines():
            matrix.append(list(map(lambda x: float(x), line.split())))
    return matrix

def mierzymy(x, macierz):
    lista=[]
    for line in range  (0,len(macierz)):
        wynik=metryka_euplidesowa(x, macierz[line])
        key=macierz[line][-1]
        lista.append((key,wynik))
    return lista

def grupujemy(lista_tupli):
    diction={}
    for line in lista_tupli:
        key=line[0]
        if key in diction:
            diction[key].append(line[1])
        else:
            diction[key]=[line[1]]
    return diction
        
def suma(slownik):
    slow={}
    listy=slownik.items()
    for tupla in listy:
        ucieta=tupla[1]
        slow[tupla[0]]=sum(ucieta)
    return slow   

def assign_random(matrix):
    for data in matrix:
        data[-1] = random.choice([0, 1])
    return matrix

matrix=readfile("australian.dat")
rand_matrix=assign_random(matrix)

def kolorki(rand_matrix):
    zmiany=1
    while zmiany!=0:
        zmiany=0
        srodek_0=None
        srodek_0_odl=None
        srodek_1_odl=None
        srodek_1=None
        for linia in rand_matrix:
            lista_tupli=mierzymy(linia, rand_matrix)
            grup=grupujemy(lista_tupli)
            suma_el=suma(grup)
            
            if srodek_0 is None:
                srodek_0=linia
                srodek_0_odl=suma_el[0]
            else:
                if suma_el[0]<srodek_0_odl:
                    srodek_0=linia
                    srodek_0_odl=suma_el[0]
                    
            if srodek_1 is None:
                srodek_1=linia
                srodek_1_odl=suma_el[1]
            else:
                if suma_el[1]<srodek_1_odl:
                    srodek_1=linia
                    srodek_1_odl=suma_el[1]
        for linia in rand_matrix:
            odl_0=metryka_euplidesowa(linia, srodek_0)
            odl_1=metryka_euplidesowa(linia, srodek_1)
            if odl_0<odl_1:
                if linia[-1]!=0:
                    linia[-1]=0
                    zmiany+=1
            if odl_1<odl_0:
                 if linia[-1]!=1:
                     linia[-1]=1
                     zmiany+=1
        print("zmiany: "+str(zmiany))
    return rand_matrix

print(kolorki(rand_matrix))