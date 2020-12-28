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
    def inp():return (int(input()))
    def minp():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def inp():return (int(stdin.readline()))
    def minp():return(map(int,stdin.readline().split()))
    
####### ---- Start Your Program From Here ---- #######
n1,n2,n3=map(int, input().split())
d={}
for i in range(n1):
    temp=int(input())
    try:
        d[temp]+=1
    except:
        d[temp]=1
for i in range(n2):
    temp=int(input())
    try:
        d[temp]+=1
    except:
        d[temp]=1
for i in range(n3):
    temp=int(input())
    try:
        d[temp]+=1
    except:
        d[temp]=1
a=[]
for keys in d:
    if d[keys]>=2:
        a.append(keys)
print(len(a))
a.sort()
for i in range(len(a)):
    print(a[i])
