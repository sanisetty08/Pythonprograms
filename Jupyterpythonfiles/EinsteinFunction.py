# coding: utf-8

# In[2]:

import math

m = 3
c = m * math.pow(10, 8)
e = int(m * math.pow(c, 2))
print(e)

# In[ ]:

# Step1:initialize m with 3
# Step2:initialize c with m*10 power 8
# Step3:assign e with required formula
# Step4:print the value for the formula
# Step5:initialize s with 5
# Step6:initialize t with s*10 power 8
# Step7:assign g with required form
# Step8:print the value for the formula
# Step9:initialize p with 9
# Step10:initialize q with p*10 power 8
# Step11:assign y with required form
# Step12:print the value for the formula


# In[6]:

import math

m = 3
c = m * math.pow(10, 8)
e = int(m * math.pow(c, 2))
print(e)

s = 5
t = s * math.pow(10, 8)
g = int(s * math.pow(t, 2))
print(g)

p = 9
q = p * math.pow(10, 8)
y = int(p * math.pow(q, 2))
print(y)

# In[11]:

import math


def shivaformula(x, y):
    shiva = int(x * math.pow(y, 2))
    return shiva  # returning for the call


def sanjayformula(z):
    sanjay = z * math.pow(10, 8)
    return sanjay


# def srinuformula(u,w):
# srinu = sanjayformula(u)
# anisetty = shivaformula(u,w)
# return anisetty

m = 3
c = sanjayformula(m)
e = shivaformula(m, c)  # calling shivaformula
print(e)

s = 5
t = sanjayformula(s)
g = shivaformula(s, t)  # calling shivaformula
print(g)

p = 9
q = sanjayformula(p)
y = shivaformula(p, q)  # calling shivaformula
print(y)
