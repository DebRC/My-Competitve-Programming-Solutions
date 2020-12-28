from sys import stdin, stdout
import math,sys
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict
from os import path
import bisect as bi
import heapq 
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
pre=[0]*100005
suff=[0]*100005
a=[0]*100001
for _ in range(inp()):
    n,q=minp()
    arr=list(minp())
    for i in range(1,n+1):
        a[i]=arr[i-1]
    pre[0],suff[n+1]=0,0
    for i in range(1,n+1):
        pre[i]=math.gcd(pre[i-1],a[i])
    for i in range(n,0,-1):
        suff[i]=math.gcd(suff[i+1],a[i])
    for i in range(q):
        l,r=map(int, input().split())
        print(math.gcd(pre[l-1],suff[r+1]))