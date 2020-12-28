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
def findXOR(n): 
    mod = n % 4
    if (mod == 0): 
        return n
    elif (mod == 1): 
        return 1
    elif (mod == 2): 
        return n + 1
    elif (mod == 3): 
        return 0
def findXORFun(l, r): 
    temp=(findXOR(l - 1)^findXOR(r))
    if temp&1:
        return "Odd"
    else:
        return "Even"
for i in range(inp()):
    l,r=minp()
    print(findXORFun(l,r))