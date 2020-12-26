from sys import stdin, stdout
import math,sys,threading
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
n,k=minp()
s=list(input())
l=list(input())
for i in range(n):
    if s[i] in l:
        s[i]=1
    else:
        s[i]=0
count=0
flag=0
total=0
for i in range(n):
    if s[i]==1:
        count+=1
    else:
        flag=1
    if flag:
        total+=(count*(count+1)//2)
        flag=0
        count=0
if count:
    total+=(count*(count+1)//2)
print(total)