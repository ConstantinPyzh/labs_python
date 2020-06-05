import math as mth
import sys
import ast

def decomp(ar):
    mas = [0]*mas_size
    i = 0
    while (i <= len(ar)-1):
        mas[mth.floor(i/mas_size)] += ar[i]
        i += 1
    return mas
  
  
  def summary(l, r, ar):
    mas_size = mth.ceil(len(ar)**(0.5))
    decomp = decomp(ar) 
    first = mth.floor(l/mas_size)
    last = mth.floor(r/mas_size)
    sum = 0
    if first == last:
        exp = l
        while (exp <= r):
            sum += ar[exp]
            exp += 1
    else:
        i = l
        while (i <= (first+1)*mas_size - 1):
            sum += ar[i]
            i += 1 
        j = last*mas_size
        while (j <= r):
            sum += ar[j]
            j += 1
        k = first + 1
        while (k <= last - 1):
            sum += mas[k]
            k += 1
    return sum
  
  
   while True:
        try:    
            ar = input("Enter array: ")
            ar = [float(x) for x in array.split()]
            break
                
            try:
                l = int(input("Enter the first number: "))
                r = int(input("Enter the last number: "))
                break
            

print("The sum of elements in the array equals ", format(summary(l, r, ar)))
