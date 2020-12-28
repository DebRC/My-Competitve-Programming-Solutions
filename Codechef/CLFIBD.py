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
    s=list(input())
    n=len(s)
    d={}
    for i in range(n):
        try:
            d[s[i]]+=1
        except:
            d[s[i]]=1
    a=[]
    for keys in d:
        a.append(d[keys])
    n=len(a)
    if n<3:
        print("Dynamic")
        continue
    flag=0
    a.sort()
    for i in range(2,n):
        if a[i]!=a[i-1]+a[i-2]:
            flag=1
            break
    if not flag:
        print("Dynamic")
    else:
        a[0],a[1]=a[1],a[0]
        for i in range(2,n):
            flag=0
            if a[i]!=a[i-1]+a[i-2]:
                flag=1
                break
        if not flag:
            print("Dynamic")
        else:
            print("Not")
        