from sys import stdin, stdout
import math,sys
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict,Counter
from os import path
import bisect as bi
import heapq 
mod=10**9+7
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
def islucky(n):
    a=list(str(n))
    a=[int(x) for x in a]
    flag=1
    for i in range(len(a)):
        if a[i]==4 or a[i]==7:
            continue
        else:
            flag=0
            break
    return flag
    
n=int(input())
flag=0
for i in range(1,n+1):
    if islucky(i):
        if n%i==0:
            flag=1
            break
if flag:
    yes()
else:
    no()