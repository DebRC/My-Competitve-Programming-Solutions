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
n=inp()
a=list(minp())
five=a.count(5)
zero=a.count(0)
if zero==0:
    print(-1)
    exit(0)
n5=five//9
for i in range(n5):
    for j in range(9):
        print(5,end="")
if n5==0:
    print(0)
    exit(0)
for i in range(zero):
    print(0,end="")
print()