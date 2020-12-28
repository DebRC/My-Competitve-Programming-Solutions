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
week={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
for _ in range(inp()):
    s,e,l,r=input().split()
    l,r=int(l),int(r)
    diff=week[e]-week[s]+1
    if diff<=0:
        diff=diff+7
    count=0
    du=0
    i=0
    while((i*7+diff)<=r):
        if (i*7+diff)>=l and (i*7+diff)<=r:
            count+=1
            du=i*7+diff
        i+=1
    if count>1:
        print("many")
    elif count==1:
        print(du)
    else:
        print("impossible")
    