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
n,k=minp()
a=list(minp())
total=0
for i in range(k):
    total+=a[i]
min_sum=total
index=0
for i in range(k,n):
    total-=a[i-k]
    total+=a[i]
    if total<min_sum:
        min_sum=total
        index=(i-k+1)
#print(min_sum)
print(index+1)