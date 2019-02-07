#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int n,m;
	cin>>n>>m;
	int a[n],c[n];
	for(int i=0;i<n;i++)
		cin>>a[i];
	for(int i=0;i<n;i++)
		cin>>c[i];
	map<int,int> mp;
	for(int i=0;i<n;i++)
		mp[i]=a[i];
	vector<pair<int,int> > vi;
	for(int i=0;i<n;i++)
	{
		vi.push_back({c[i],i});
	}
	sort(vi.begin(),vi.end());
	int cur=0;
	for(int I=0;I<m;I++)
	{
		long long ans=0;
		int flag=0;
		int t,d;
		cin>>t>>d;
		if(mp[t-1]>=d)
		{
			ans+=(d*(c[t-1]));
			mp[t-1]-=d;
		}
		else
		{
			ans+=mp[t-1]*c[t-1];
			int rem = d-mp[t-1];
			mp[t-1]=0;
			while(rem!=0)
			{
				if(cur>=n-1)
					break;
				for(int i=cur;i<n;i++)
				{
					if(mp[vi[i].second]>=rem)
					{
						ans+=rem*c[vi[i].second];
						mp[vi[i].second]-=rem;
						rem=0;
					}
					else
					{
						ans+=mp[vi[i].second]*c[vi[i].second];
						rem-=mp[vi[i].second];
						mp[vi[i].second]=0;
						cur+=1;
					}
				}
			}
			if(rem)
				flag=1;
		}
		if(flag)
			cout<<0<<"\n";
		else
			cout<<ans<<"\n";
	}
}
