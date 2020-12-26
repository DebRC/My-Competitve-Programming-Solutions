import sys
import threading
from collections import defaultdict

n,m=list(map(int,input().split()))
cat=list(map(int,input().split()))
adj=defaultdict(list)
for _ in range(n-1):
    p,c=list(map(int,input().split()))
    adj[p].append(c)
    adj[c].append(p)

    
def fun(root,par,cnt):
    if cnt==m and cat[root-1]:
        return 0
    if len(adj[root])==1 and adj[root][0]==par:
        return 1
    ans=0
    for ch in adj[root]:
        if ch != par:
              ans+=fun(ch,root,cnt+1 if cat[root-1] else 0)
    return ans
def main():
    print(fun(1,0,0))
if __name__=="__main__":
    sys.setrecursionlimit(10**6)
    threading.stack_size(10**8)
    t = threading.Thread(target=main)
    t.start()
    t.join() 