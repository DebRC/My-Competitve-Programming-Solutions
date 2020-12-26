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
def small(n,s):
    a=[0]*n
    if n*9<s:
        return -1
    if s==0 and n>1:
        return -1
    if s==0:
        return 0
    s-=1
    i=n-1
    while(i>0):
        if s>=9:
            a[i]=9
            s-=9
        else:
            a[i]=s
            s=0
        i-=1
    a[0]=s+1
    a=[str(x) for x in a]
    #print(a)
    return "".join(a)
def large(n,s):
    a=[0]*n
    if n*9<s:
        return -1
    if s==0 and n>1:
        return -1
    if s==0:
        return 0
    i=0
    while(s>0 and i<n):
        if s>9:
            a[i]=9
            s-=9
            i+=1
        else:
            a[i]=s
            s=0
    if s:
        return -1
    a=[str(x) for x in a]
    #print(a)
    return "".join(a)
def main():
    m,s=minp()
    print(small(m,s),large(m,s))
main()