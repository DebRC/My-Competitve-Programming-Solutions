#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		long long n,i;
		cin>>n;
		long long a[n],b[n];
		unordered_map<long long int,long long int> total_1;
		unordered_map<long long int,long long int> total_2;
		unordered_map<long long int,long long int> total_3;
		vector<long long int> m1,m2;
		long long minimum=100000000000;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		for(i=0;i<n;i++)
		{
			cin>>b[i];
			
		}
		for(i=0;i<n;i++)
		{
			total_1[a[i]]++;
			total_1[b[i]]++;
			minimum=min(a[i],minimum);
			minimum=min(b[i],minimum);
		}
		int odd=0;
		for(auto i:total_1)
		{
			if(i.second%2==0)
			{
				total_2[i.first]=i.second/2;
			}
			else
			{
				odd=1;
				break;
			}
		}
		if(odd==1)
		{
			cout<<"-1"<<endl;
			continue;
		}
		total_3=total_2;
		for(i=0;i<n;i++)
		{
			if(total_3[a[i]]==0)
			{
				m1.push_back(a[i]);
			}
			else
			{
				total_3[a[i]]--;
			}
		}
		if(m1.size()==0)
		{
			cout<<"0"<<endl;
			continue;
		}
		total_3=total_2;
		for(i=0;i<n;i++)
		{
			if(total_3[b[i]]==0)
			{
				m2.push_back(b[i]);
			}
			else
			{
				total_3[b[i]]--;
			}
		}
		if(m1.size()!=m2.size())
		{
			cout<<"-1"<<endl;
			continue;
		}
		long long int count=0;
		sort(m1.begin(),m1.end(),greater<long long int>());
		sort(m2.begin(),m2.end());
		for(i=0;i<m2.size();i++)
		{
			count+=min(min(m1[i],m2[i]),2*minimum);
		}
		cout<<count<<endl;
	}
return 0;
}