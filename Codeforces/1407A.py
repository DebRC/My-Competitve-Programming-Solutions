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
    odd_sum=0
    even_sum=0
    for i in range(1,n+1):
        if i&1:
            odd_sum+=a[i-1]
        else:
            even_sum+=a[i-1]
    if odd_sum==even_sum:
        print(n)
        print(*a)
        continue
    count_1=0
    count_0=0
    for i in range(n):
        if a[i]==0:
            count_0+=1
        else:
            count_1+=1
    if count_0>=n//2:
        print(n//2)
        for i in range(n//2):
            print(0,end=" ")
    else:
        if (n//2)&1:
            print(n//2+1)
            for i in range(n//2+1):
                print(1,end=" ")
        else:
            print(n//2)
            for i in range(n//2):
                print(1,end=" ")
    print()