#!/usr/bin/env python3


#Bubble sorted
import time
import math



def bubble_sort(a):
  
  iterations = 0
  a = list(a)
  x = a.copy()
  y = 0
  for g in range(len(x)**2):
   
    z = x[y]
    u = x[y+1]
    
    if z > u:
      
      x[y+1] = z
      x[y] = u

      

    elif z < u:
      pass
    
    
    
    
    
    y = y + 1
    if y+1 == len(a):
      y = 0
    
    iterations += 1

  print(x)
  iterations = int(math.sqrt(iterations)-1)
  iterations = str(iterations)
  print(iterations + " iterations")
  print("Iterations mean the # of times the code had to go through the loop to sort the entire thing.")

lary = input("Give a list that you want to be sorted: ")
start_time = time.time()
bubble_sort(lary)




print(str(time.time() - start_time) + " seconds!")




  
