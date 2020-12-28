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
    freq1=Counter(a)
    #print(freq1)
    freq2={}
    for keys in freq1:
        try:
            freq2[freq1[keys]]+=1
        except:
            freq2[freq1[keys]]=1
    #print(freq2)
    mode=999999
    mode_value=0
    for keys in freq2:
        if freq2[keys]>mode_value:
            mode=keys
            mode_value=freq2[keys]
        elif freq2[keys]==mode_value and keys<mode:
            mode=keys
            mode_value=freq2[keys]
        #print(mode,mode_value)
    print(mode)