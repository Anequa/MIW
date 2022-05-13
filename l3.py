
    
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:54:44 2022

@author: Ania
"""
import numpy as np
from math import sqrt,floor,ceil
from random  import random, uniform,choice
macierz=[]
with open("australian.dat", "r", encoding="utf-8") as f:
    for line in f:
        macierz.append(list(map(lambda x:float(x),line.split())))
 
    
# for x in range(6):
#     print(macierz[x])
    
# strwórz tablice z nazwami miast olsz gdansk warszawa sosnowiec
# za pomoca map i lambdy 3 pierwsze litery

# miasta=["olsztyn","gdansk","warszawa","sosnowiec"]
# result = map(lambda x: x[:3],miasta)
# print(list(result))

# 2 listy z argumentami 
x=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
y=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
a=macierz[0]
b=macierz[5]
c=macierz[10]
d=macierz[20]
def metryka_euplidesowa(a,b):
    c=0
    leng=max(len(a),len(b))-1
    for i in range (leng):
            el=pow(a[i]-b[i],2)
            c+=el
    return sqrt(c)


def metryka_euplidesowa_2(a,b):
    l1=np.array(a)
    l2=np.array(b)
    l3=l2-l1
    iloczyn=np.dot(l3,l3)
    return sqrt(iloczyn)
    

# print(metryka_euplidesowa(a, d))
print(metryka_euplidesowa_2(a, d))
# tupla=(2,4)
# print(tupla[1])
def dic_decision(macierz,x):
        diction={}
        for line in range (0,len(macierz)):
              wynik=metryka_euplidesowa_2(x, macierz[line])
              key=macierz[line][-1]
              if key in diction:
                  diction[key].append(wynik)
              else:    
                  diction[key]=[wynik]
        return diction
slownik=dic_decision(macierz, x)
# print(slownik[0][:5])
# print(slownik[1][:5])
# print(list(slownik.values())[0][0])

def mierzymy(x, macierz):
    lista=[]
    for line in range  (0,len(macierz)):
        wynik=metryka_euplidesowa_2(x, macierz[line])
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
        
pogrupowany=grupujemy(mierzymy(x,macierz))


def suma(slownik,k):
    slow={}
    listy=slownik.items()
    for tupla in listy:
        tupla[1].sort()
        ucieta=tupla[1][:k]
        slow[tupla[0]]=sum(ucieta)
    return slow   


def dopasuj(slownik):
        lista=(sorted(slownik.items(),key=lambda x:x[1]))
        if len(lista)==1:
            return lista[0][0]
        if lista[0][1]==lista[1][1]:
            return None
        else:
            return lista[0][0]
        
        
# print(dopasuj(suma(pogrupowany,5)))
# print(pogrupowany)

def zamien(macierz):
    for i in macierz:
        if len(i)==15:
            i[-1]=choice([0,1])
    return macierz

            
def segregacja(macierz):
    slownik={}
    for i in macierz:
        if i[-1] in slownik:
            slownik[i[-1]].append(i)
        else:    
            slownik[i[-1]]=[i]
    return slownik

m=zamien(y)
print(m)
print(segregacja(m))
def odleglosci(slownik):
    list1=[]
    list2=[]
    for i in slownik[0][0]:
        for j in slownik[0][0]:
           list1.append(metryka_euplidesowa_2(i, j))
    for i in slownik[1][0]:
        for j in slownik[1][0]:
           list2.append(metryka_euplidesowa_2(i, j))
    print(list1)
    list1.sort()
    list2.sort()
    print(list1)
print(odleglosci(segregacja(m)))
        

       
def root (x):
    return x


def funcIn(x, y,function):
    if y > 0 and y <= function(x):
        return 1
    elif y < 0 and y >= function(x):
        return -1
    return 0

def randomPoint(a,b):
    return uniform(a, b)

def monteCarlo(xp, xk, func, numberOfPoints):
    pointsIn = 0
    yp = min(func(xp),func(xk))
    yk = ceil(max(func(xp),func(xk)))
    
    for i in range(numberOfPoints):
        pointsIn += funcIn(randomPoint(xp, xk),randomPoint(yp, yk),func)
        
    integral = pointsIn/numberOfPoints*(xk-xp)*(yk-yp)
    return integral

print(monteCarlo(0, 1, root, 10000))
# n=ilosc trapezów
# def trapez(fun, a, b, n):
#   suma_trapezu = 0
#   dx  = (b-a)/n
 
#   for i in range(n):
#     fa = a + dx * i
#     fb = a + dx * (i + 1)
#     suma_trapezu += (fun(fa) + fun(fb)) / 2 * dx
#   return suma_trapezu
 
def trapez(fun, a, b, epsylon):
  suma_trapezu = 0
  pop_sum=0
  frequency=1
  while True:
      dx  = (b-a)/frequency
      suma_trapezu=0
      for i in range(frequency):
          fa = a + dx * i
          fb = a + dx * (i + 1)
          suma_trapezu += (fun(fa) + fun(fb)) / 2 * dx
          r=abs(pop_sum-suma_trapezu) 
      if r<=epsylon:
            return suma_trapezu
          
      else:
            pop_sum=suma_trapezu
            frequency+=frequency
 
integral = trapez(root, 0, 1, 0.00000000000001)
print(integral)