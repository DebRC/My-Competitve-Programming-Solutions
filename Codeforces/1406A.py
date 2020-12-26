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
for _ in range(inp()):
    n=inp()
    a=list(minp())
    if 0 not in a:
        print(0)
        continue
    a.sort()
    if a.count(0)==1:
        for i in range(n+1):
            if i not in a:
                flag=i
                break
        print(flag)
        continue
    flag=False
    for i in range(n+1):
        if a.count(i)==0:
            t1=2*i
            break
        if a.count(i)==1:
            flag=True
            t1=i
            break
    t2=0
    if flag:
        for i in range(n+1):
            if i not in a:
                t2=i
                break
    print(t1+t2)