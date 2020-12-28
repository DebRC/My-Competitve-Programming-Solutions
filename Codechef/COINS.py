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
a = {}
a[0]=0
def coin(n):
    if n not in a:
        a[n]=max(coin(n//2)+coin(n//3)+coin(n//4),n)
    return a[n]
    
while True:
    try:
        n = int(input())
        print(coin(n))
    except:
        break