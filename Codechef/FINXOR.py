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
    xor_list=[]
    for i in range(1,21):
        print(1,(1<<i),flush=True)
        xor_list.append(inp())
    xor_list.reverse()
    k=xor_list[0]-n*(1<<20)
    #print(len(xor_list))
    for i in range(1,20):
        if xor_list[i]<=k:
            xor_list[i]=(n+(k-xor_list[i])//(1<<(20-i)))//2
        else:
            xor_list[i]=(n-(xor_list[i]-k)//(1<<(20-i)))//2
    xor_sum=0
    for i in range(1,20):
        if xor_list[i]&1:
            xor_sum+=(1<<(20-i))
    if(k&1):
        xor_sum+=1
    print(2,xor_sum,flush=True)
    if inp()==-1:
        exit(0)