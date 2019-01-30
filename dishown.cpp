#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int par[100005];
vector<ll> arr(100005);

void make_par(int u, ll val){
	par[u] = u;
	arr[u] = val;
}

int find(int x){
	return par[x] = (par[x]==x)?x : find(par[x]);
}
void merge(int x, int y){
	x = find(x);
	y = find(y);
	if(x == y){
		cout<<"Invalid query!"<<endl;
		return;
	}
	if(arr[x]<arr[y])
		swap(x,y);
	if(arr[x] == arr[y])
		return;
	par[y] = x;
}


int main(){
	int t, type, n, q,x,y;	
	
	cin>>t;
	while(t--){
		ll arr;
		cin>>n;

		for(int i=1;i<=n;i++){
			cin>>arr;
			make_par(i,arr);
		}
		
		cin>>q;
		while(q--){
			cin>>type;
			if(type){
				cin>>x;
				cout<<find(x)<<endl;
			}
			else{
				cin>>x>>y;
				merge(x,y);
			}
		
		}
	
}
}
