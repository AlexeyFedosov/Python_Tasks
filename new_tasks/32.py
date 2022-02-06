from math import dist
from tkinter import N
from turtle import left

def mix(n):   
    dict = {}
    for k in range(1, n+1):
        dict[k] = 3*k + 1
    print(dict)
mix(5)