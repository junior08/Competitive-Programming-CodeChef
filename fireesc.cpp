#include<bits/stdc++.h>
using namespace std;
 
long long int par[100005];
long long int s[100005];
 
int find(int x){#finds the parent
	return par[x]=(par[x]==x)?x:find(par[x]);
}
 
int merge(int x, int y){#merges the indices 
	if(x > y)
		swap(x, y);
	par[find(x)] = find(y);
	/*if(find(x)<find(y)){
		par[find(y)]=find(x);
	}
	else{
		par[find(x)]=find(y);
	}*/
}
 
int main(){
	int t, n, m, a, b;
	long long int leaders;
	long long int num_of_sets;
	std::ios_base::sync_with_stdio(false);
	cin>>t;
	while(t--){
		cin>>n>>m;
		leaders = 1;
		num_of_sets = 0;
		for(int i=1;i<=n;i++){
			par[i]=i;
			s[i]=0;
		}
		
		for(int i = 1;i <= m;i++){
			cin>>a>>b;
			merge(a,b);
		}

		for(int i = 1;i <= n;i++){
			s[find(i)] += 1;
			if(find(i) == i){
				num_of_sets++;
			}
		}
		
		for(int i = 1;i <= n;i++){
			if(s[i]>0)
				leaders *= s[i];
			leaders %= 1000000007;
		}
		cout<<num_of_sets<<" "<<leaders<<endl;
	}
}  
