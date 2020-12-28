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
def find_le(a, x):
    i = bi.bisect_right(a, x)
    if i:
        return i-1
    else:
        return -1
for _ in range(I()):
    try:
        n=I()
        a=list(In())
        a.sort()
        q=I()
        for i in range(q):
            x,y=In()
            res=x+y
            temp=find_le(a,res)
            if temp==-1:
                print(0)
            else:
                if a[temp]==res:
                    print(-1)
                else:
                    print(temp+1)
    except:
        pass