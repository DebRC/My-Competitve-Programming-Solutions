#include<bits/stdc++.h>
using namespace std;
char a[1001][1001];
bool visited[1001][1001];
int n, m;

bool isValid(int i, int j)
{
    if (i < 0 or j < 0 or i >= n or j >= m)
        return false;
    if (a[i][j] == '#' or visited[i][j])
        return false;
    return true;
}

void dfs(int i, int j)
{
    visited[i][j] = true;
    if (isValid(i - 1, j))
        dfs(i - 1, j);
    if (isValid(i, j + 1))
        dfs(i, j + 1);
    if (isValid(i + 1, j))
        dfs(i + 1, j);
    if (isValid(i, j - 1))
        dfs(i, j - 1);
}

int main()
{
    cin>>n>>m;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
         cin>>a[i][j];
    int count {0};
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if (a[i][j]=='.' && !visited[i][j])
            {
                dfs(i,j);
                count+=1;
            }
    cout<<count<<endl;
    return 0;
}