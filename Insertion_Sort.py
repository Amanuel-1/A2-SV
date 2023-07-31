#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
  # Define the print function
  def print_arr():
      s = ""
      for k in range(n):
          s += str(arr[k]) + " " if k != n-1 else str(arr[k])
      print(s)
  
  # Call print_arr to print the initial array

  
  j = n - 2
  e = arr[n-1]
  while j >= 0 and arr[j] > e:
      arr[j+1] = arr[j]
      print_arr()
      j -= 1
  arr[j+1] = e
  print_arr()
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
