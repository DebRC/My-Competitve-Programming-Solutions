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
    sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
    def inp():return (int(input()))
    def minp():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def inp():return (int(stdin.readline()))
    def minp():return(map(int,stdin.readline().split()))
    
####### ---- Start Your Program From Here ---- #######
for _ in range(inp()):
    n,k=minp()
    a=list(minp())
    for i in range(n):
        a[i]-=k
    flag=False
    for i in range(n):
        if i!=0:
            a[i]=a[i]+a[i-1]
        if a[i]<0:
            index=i+1
            flag=True
            break
    if flag:
        print(index)
    else:
        print(n+(a[n-1]//k)+1)