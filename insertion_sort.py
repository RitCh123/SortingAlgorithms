#!/usr/bin/env python3
import time
from termcolor import cprint


def insertion_sort(arr):
  global iterations

  iterations = 0
  arr = list(arr)
  x = []
  y = arr.copy()

  list_index = 0
  for i in range(len(arr)**len(arr)):
    if list_index + 1 == len(arr):
        cprint("Search complete", "green")
        break

      
    if arr[list_index] > arr[list_index + 1]:
      list_index += 1
      y = list_index
      
      if list_index <= 1:

      
        arr[y], arr[y - 1] = arr[y - 1], arr[y]
        iterations += 1
      
      elif list_index > 1:
        
        while arr[y] < arr[y-1]:

          arr[y], arr[y-1] = arr[y-1], arr[y]
          iterations += 1
          y -= 1
          if y == 1 and arr[y] < arr[y-1]:
            arr[y], arr[y-1] = arr[y-1], arr[y]
            iterations += 1
            break


      
    
    elif arr[list_index] < arr[list_index + 1]:
      list_index += 1
      iterations += 1
    
  print(arr)
  cprint(str(iterations) + " iterations!", "red")


lary = input("Give a list to be sorted: ")
insertion_sort(lary)
