from sys import stdin, stdout
import math,sys
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict
from os import path
import bisect as bi
import heapq 
def yes():print('YES')
def no():print('NO')
if (path.exists('input.txt')): 
    #------------------Sublime--------------------------------------#
    sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
    def I():return (int(input()))
    def In():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def I():return (int(stdin.readline()))
    def In():return(map(int,stdin.readline().split()))
    
####### ---- Start Your Program From Here ---- #######
for _ in range(I()):
    n,m=In()
    a=[]
    for i in range(n):
        temp=list(input())
        a.append(temp)
    cost1=0
    cost2=0
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0:
                if a[i][j]=="G":
                    cost1+=3
                else:
                    cost2+=5
            else:
                if a[i][j]=="R":
                    cost1+=5
                else:
                    cost2+=3
    print(min(cost1,cost2))