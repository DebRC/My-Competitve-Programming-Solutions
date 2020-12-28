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
    # sortedd=True
    # for i in range(n-1):
    #     if a[i]>=a[i+1]:
    #         sortedd=False
    #         break
    # if sortedd:
    #     print(1,1)
    #     continue
    # reversedd=True
    # for i in range(n-1):
    #     if a[i]<=a[i+1]:
    #         reversedd=False
    #         break
    # if reversedd:
    #     print(n,n)
    #     continue
    # if len(set(a))==1:
    #     print(1,1)
    #     continue
    infected_list=[]
    for i in range(n):
        infected=[0]*n
        for j in range(n):
            if a[j]>a[i] and j<i:
                infected[j]=(i-j)/(a[j]-a[i])
            if a[j]<a[i] and j>i:
                infected[j]=(j-i)/(a[i]-a[j])
        infected_list.append(infected)
    max_infect=0
    min_infect=6
    for i in range(n):
        infected=[0]*n
        infected[i]=1
        for j in range(n):
            if infected_list[i][j]>0:
                time=infected_list[i][j]
                infected[j]=1
                for k in range(n):
                    if infected_list[j][k]>=time:
                        infected[k]=1
        #print(infected)
        if sum(infected)>max_infect:
            max_infect=sum(infected)
        if sum(infected)<min_infect:
            min_infect=sum(infected)
    print(min_infect,max_infect)