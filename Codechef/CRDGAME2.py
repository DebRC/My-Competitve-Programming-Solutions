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
    if n==1:
        print(2)
        continue
    result=(pow(2,n,mod))%mod
    max_ele_freq=a.count(max(a))
    if max_ele_freq&1:
        print(result%mod)
        continue
    rep_combination=1
    for i in range(max_ele_freq//2):
        rep_combination = (((rep_combination%mod*(max_ele_freq-i)%mod)%mod)*pow(i+1,mod-2,mod)%mod)%mod
    total_comb=((pow(2,n-max_ele_freq,mod))%mod*rep_combination%mod)%mod
    print((result-total_comb)%mod)