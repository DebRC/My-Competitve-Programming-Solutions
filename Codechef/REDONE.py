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
l=[0]*(10**6+1)
l[1]=1
for i in range(2,1000001):
    l[i]=((l[i-1]+i)%mod+(l[i-1]*i)%mod)%mod
for _ in range(inp()):
    n=inp()
    print(l[n])