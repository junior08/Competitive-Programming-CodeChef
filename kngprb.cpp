#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int> pi;
#define INF 0x3f3f3f3f

void dij(int source,int n,vector< pi > a[],long long dist[])
{
	priority_queue<pi,vector<pi>,greater<pi> > q;
	dist[source]=0;
	q.push({0,source});
	while(!q.empty())
	{
		int u = q.top().second;
		q.pop();
		for(auto c:a[u])
		{
			int v= c.first;
			int w= c.second;
			if(dist[v]>dist[u]+w)
			{
				dist[v]=dist[u]+w;
				q.push({dist[v],v});
			}
		}
	}
		
}

int main(){
	ios_base::sync_with_stdio(false);
	long long t, n, m, source, dest, a, b, u, v;
	
	cin>>t;
	while(t--){
		cin>>n>>m;
		vector< pi > a[n+2];
		long long dist[n+2];
		memset(dist,INF,sizeof(dist));
		
		for(int i = 0; i < m; i++){
			cin>>u>>v;
			a[u].push_back({v, 0});
			a[v].push_back({u, 1});
				
		}
		cin>>source>>dest;
		dij(source, n, a, dist);
		
		
		if(dist[dest] > n) 
			cout<<-1<<"\n";
		else 
			cout<<dist[dest]<<"\n";
		
	} 
}


