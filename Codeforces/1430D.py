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
    a=list(map(int, input()))
    #print(a)
    b=[]
    count=1
    for i in range(1,n):
        #print(b)
        if a[i]!=a[i-1]:
            b.append(count)
            count=1
        else:
            count+=1
    if count>0:
        b.append(count)
    #print(b)
    n=len(b)
    if n==1:
        print(1)
        continue
    op=0
    head=0
    tail=0
    if b[0]>1:
        op+=1
        b[head]=0
        head+=1
        tail+=1
    #print(b,head,tail,n)
    while(head<n):
        if b[head]==1:
            head+=1
            continue
        if b[head]>1 and b[head-1]==0:
            b[head]=0
            head+=1
            tail+=1
            op+=1
            continue
        if b[head]>1:
            b[head]-=1
            b[tail]-=1
            tail+=1
            op+=1
            if b[head]==1:
                head+=1
    print(op+math.ceil((b.count(1))/2))