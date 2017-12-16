#!/usr/bin/env/ python3

import sys

def perm(list, i, n):
    if error(list[0:i]): return 0
    if i == n:
        for i in range(n):
            for j in range(n+1):
                if j == list[i]: print("Q|",end='')
                else: print(" |",end='')
            print()
        print()

    else:
        for j in range(i, n):
            list[i], list[j] = list[j], list[i]
            perm(list, i+1, n)
            list[j], list[i] = list[i], list[j]

def error(list):
    for i in range(1, len(list)):
        for j in range(0, i):
            if abs(list[i]-list[j]) == abs(i-j):
                return True
            
if __name__ == '__main__':
    n = int(sys.argv[1])
    list = [x+1 for x in range(n)]
    perm(list, 0, n)
