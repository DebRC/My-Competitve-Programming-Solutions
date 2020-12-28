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
import math
for _ in range(int(input())):
    a,b,n=map(int,input().split())
    m=10**9+7
    mod=m if a==b else abs(a-b)
    t=pow(a,n,mod)+pow(b,n,mod)
    t_1=math.gcd(abs(a-b),t)%(10**9+7)
    print(t_1)