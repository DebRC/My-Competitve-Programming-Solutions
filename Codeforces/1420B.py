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
def msb(n):
    k=(int)(math.log(n,2))
    return (int)(pow(2, k))

for _ in range(inp()):
    n=inp()
    a=list(minp())
    for i in range(n):
        a[i]=msb(a[i])
    d=Counter(a)
    count=0
    for keys in d:
        if d[keys]>=2:
            count+=(d[keys]*(d[keys]-1)//2)
    #print(*a)
    #print(d)
    print(count)
    