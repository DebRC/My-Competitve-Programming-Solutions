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
    zeros=[]
    count=0
    for i in a:
        if i==0:
            count+=1
        elif i==1 and count>0:
            zeros.append(count)
            count=0
    if count>0:
        zeros.append(count)
    #print(zeros)
    if len(zeros)==0:
        print("No")
        continue
    if len(zeros)==1:
        if zeros[0]&1:
            print("Yes")
        else:
            print("No")
        continue
    zeros.sort(reverse=True)
    large1=zeros[0]
    large2=zeros[1]
    if large1&1 and large2<(large1+1)//2:
        print("Yes")
    else:
        print("No")