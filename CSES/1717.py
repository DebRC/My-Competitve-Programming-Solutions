from sys import stdin, stdout
import math,sys
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict,Counter
from os import path
import bisect as bi
import heapq 
def yes():print('YES')
def no():print('NO')
if (path.exists('input.txt')): 
    #------------------Sublime--------------------------------------#
    sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w')
    def inp():return (int(input()))
    def minp():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def inp():return (int(stdin.readline()))
    def minp():return(map(int,stdin.readline().split()))
    
####### ---- Start Your Program From Here ---- #######
mod=10**9+7
def countDer(n):
    der = [0]*(n + 1)
    der[0] = 1
    der[1] = 0
    der[2] = 1
    for i in range(3, n + 1): 
        der[i] = ((i - 1)*(der[i - 1] + der[i - 2])%mod)%mod
    return der[n]%mod
n=inp()
print(countDer(n))