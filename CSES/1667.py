import sys
import queue

def minEdgeBFS(edges, n):
    previous=[0]*(n+1)
    q=queue.Queue()
    q.put(1)
    previous[1]=-1
    while not q.empty():
        x=q.get()
        if x==n:
            break
        for i in edges[x]:
            if not previous[i]:
                previous[i]=x
                q.put(i)
    if previous[n]:
        a=[]
        a.append(n)
        p=previous[n]
        while(p!=-1):
            a.append(p)
            p=previous[p]
        print(len(a))
        print(*a[::-1])
    else:
        print("IMPOSSIBLE")


def addEdge(edges, u, v):
    edges[u].append(v)
    edges[v].append(u)


if __name__ == "__main__":
    n,m=map(int,input().split())
    edges={}
    for i in range(1,n+1):
        edges[i]=[]
    for i in range(m):
        a,b=map(int, input().split())
        addEdge(edges,a,b)
    #print(edges)
    minEdgeBFS(edges,n)