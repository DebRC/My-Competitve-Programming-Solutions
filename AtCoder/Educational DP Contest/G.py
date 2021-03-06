import sys
sys.setrecursionlimit(1<<30)
def dfs(node, adj, dp, vis): 
    vis[node] = True 
    for i in range(0, len(adj[node])):
        if not vis[adj[node][i]]: 
            dfs(adj[node][i], adj, dp, vis)   
        dp[node] = max(dp[node], 1 + dp[adj[node][i]])  
    
def addEdge(adj, u, v):
    adj[u].append(v)  
     
def findLongestPath(adj, n):
    dp = [0] * (n + 1)  
    vis = [False] * (n + 1)
    for i in range(1, n + 1):   
        if not vis[i]:  
            dfs(i, adj, dp, vis)
    ans = 0
    for i in range(1, n + 1):   
        ans = max(ans, dp[i]) 
    return ans  

if __name__ == "__main__":  
    n,m = map(int, input().split())
    a=[[] for _ in range(n+1)]
    for i in range(m):
        q,w=map(int, input().split())
        addEdge(a,q,w)
    print(findLongestPath(a, n)) 