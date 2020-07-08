#!/usr/bin/env python3

from termcolor import cprint

def selection_sort(arr):
  arr = list(arr)
  x = []
  global itera
  itera = 1

  for i in range(0, len(arr)):
    j = 0
    e = min(arr)
    
    c = arr.index(e)
    o = arr[c]
    p = arr[len(arr)-1]
    arr[c] = p
    arr[len(arr)-1] = p
    arr.remove(arr[c])
    x.append(e)
    j += 1
    itera += 1
  cprint(x, "green")
  cprint(str(itera) + " iterations!", "blue")

lary = input("Give a list you want to sort: ")
selection_sort(lary)

