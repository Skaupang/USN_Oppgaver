# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:08:13 2021

Forelesning
"""

#%% oppgave 1a
import numpy as np 

r = 5

ar = np.pi * r **2

omk = 2 * np.pi * r

print('Areal av sirkelen med radius ', r,' =', ar )
print('Omkrets av sirkelen med rasius', r, '=' ,omk )

#denne klarte jeg selv

#%% oppgave 1b
import numpy as np

def sirkel (r):
    ar = np.pi * r **2

    omk = 2 * np.pi * r
    
    return ar, omk

    
sirkel(r)

print('sirkelen sitt Areal og omkrets er : ',sirkel(r))

#denne klarte jeg selv

#%% oppgave 1c

import numpy as np

def sirkel (r):
    ar = np.pi * r **2

    omk = 2 * np.pi * r
    
    return ar, omk


summen = 0 

for r in range (1,11):
    arealet, om = sirkel(r)
    summen += arealet



print('sirkelen sitt Areal og omkrets er : ',sirkel(r))
print(summen)
#klarer nesten alt selv
#%% oppgave 1d
import numpy as np

def sirkel (r):
    ar = np.pi * r **2

    omk = 2 * np.pi * r
    
    return ar, omk

r = 1 
arealet, omkretsen = sirkel(r)

while arealet <= 10 * omkretsen:
    r+=1
    arealet, omkretsen = sirkel(r)
    
print('Når r = ', r, 'så er arealet 10 ganger så stort som omkretsen')

#%% oppgave 2a

def ReLu (x):
    val = 0
    if x > 0  :
        val = x
        
    return val 

#klarte 80% selv

#%% oppgave 2b 

import numpy as np 
import matplotlib.pyplot as plt


def ReLu (x):
    val = 0
    if x > 0  :
        val = x
        
    return val 

x_vals = np.linspace(-1,1,100)
y_vals = np.linspace(-1,1,100)

for i in range(100):
    y_vals[i] = ReLu(x_vals[i])


plt.plot(x_vals, y_vals)

#%% 3 a 

n = 2
sum = 0 

for i in range(1, n+1):
    sum = 1 / i
    
#%% 3 b
 
n = 0 
sum = 0 

while sum < 10:
    n+=1
    sum += 1/n
    
print(n)

#%% 4 - 1 
import numpy as np 

def areal(a,b):
     radius = a / 2
     areal_sirkel = np.pi * radius**2
     areal_rektangel = a * b
     tot_areal = areal_sirkel + areal_rektangel
     return tot_areal
 
a = 0
b = 1 

min_areal = np.inf
minA = 0
minB = 0

while(a <= 1):
    tot_areal = areal(a,b)
    if (tot_areal < min_areal):
        min_areal = tot_areal
        minA = a 
        minB = b 
    a = a + 0.01
    b = b - 0.01

print('det minste arealet er', min_areal,
      'da er a:', a,' og b er: ', b)




































































