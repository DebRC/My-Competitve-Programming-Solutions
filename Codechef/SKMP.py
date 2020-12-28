from sys import stdin, stdout
import math,sys,copy
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
def BinarySearch(a, x): 
    i = bi.bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1
for _ in range(int(input())):
    s=list(input())
    p=list(input())
    for i in range(len(p)):
        s.remove(p[i])
    temp=copy.deepcopy(s)
    temp.append(p[0])
    temp.sort()
    temp.reverse()
    s.sort()
    #print(s)
    #print(ne)
    str1=''.join(s[:len(temp)-temp.index(p[0])-1])+''.join(p)+''.join(s[len(temp)-temp.index(p[0])-1:])
    if BinarySearch(s, p[0])!=-1:
        str2=''.join(s[:s.index(p[0])])+''.join(p)+''.join(s[s.index(p[0]):])
        print(min(str1,str2))
    else:
        print(str1)