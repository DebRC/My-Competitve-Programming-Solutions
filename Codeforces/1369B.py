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
for _ in range(inp()):
    n=inp()
    s=list(input())
    s=[int(x) for x in s]
    if s==sorted(s):
        print(*s,sep="")
        continue
    count_0=1
    count_1=0
    i=0
    while(s[i]!=1 and i<n):
        count_0+=1
        i+=1
    i=n-1
    while(s[i]!=0 and i>=0):
        count_1+=1
        i-=1
    for i in range(count_0):
        print(0,end="")
    for i in range(count_1):
        print(1,end="")
    print()
    