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
    count=0
    for i in range(n):
        count+=a[i]
    #print(test)
    if count!=0:
        print("YES")
        new=[]
        for i in range(n):
            if a[i]!=0:
                new.append(a[i])
        #print(new,count)
        if count>0:
            new.sort(reverse=True)
            for i in range(n-len(new)):
                new.append(0)
        else:
            new.sort()
            for i in range(n-len(new)):
                new.append(0)
        print(*new)
    else:
        print("NO")