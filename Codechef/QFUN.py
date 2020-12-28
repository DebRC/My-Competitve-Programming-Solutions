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
def countSubstr(s, n, x, y): 
    total=0
    total_x=0
    for i in range(n):  
        if s[i] == x: 
            total_x += 1
        if s[i] == y: 
            total += total_x 
    return total 

for _ in range(inp()):
    n=inp()
    s=input()
    x='0'
    y='1'
    x1='1'
    y1='0'
    c1=countSubstr(s,n,x,y)
    c2=countSubstr(s,n,x1,y1)
    print(c1+c2)