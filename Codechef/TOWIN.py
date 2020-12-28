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
    a.sort(reverse=True)
    if n==1:
        print("first")
        continue
    if n==2:
        if a[0]>a[1]:
            print("first")
        elif a[0]<a[1]:
            print("second")
        else:
            print("draw")
        continue
    first=a[0]
    second=a[1]+a[2]
    for i in range(3,n,2):
        first+=a[i]
    for i in range(4,n,2):
        second+=a[i]
    if first>second:
            print("first")
    elif first<second:
        print("second")
    else:
        print("draw")