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
    n=inp()
    a=list(minp())
    triplet=False
    doublet=False
    hmap={}
    for i in a:
        try:
            hmap[i]+=1
            if hmap[i]==3:
                triplet=True
                break
            if hmap[i]==2:
                doublet=True
        except:
            hmap[i]=1
    if triplet:
        no()
        continue
    if not doublet:
        yes()
        print(*sorted(a))
        continue
    result1=[]
    for keys in hmap:
        result1.append(keys)
        hmap[keys]-=1
    result2=[]
    for keys in hmap:
        if hmap[keys]==1:
            result2.append(keys)
    result1.sort()
    result2.sort(reverse=True)
    result1.extend(result2)
    side=False
    for i in range(1,n):
        if result1[i]==result1[i-1]:
            side=True
    if side:
        no()
    else:
        yes()
        print(*result1)