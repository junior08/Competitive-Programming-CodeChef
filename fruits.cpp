#include <bits/stdc++.h>
using namespace std;

int main(){
	int t, n, m, k;
	cin>>t;
	
	while(t--){
		
		cin>>n>>m>>k;
		
		if(k + min(n, m) > max(n, m)){
			cout<<0<<endl;
			continue;
		}
		
		int ans = max(n, m) - (min(n, m) + k);
		cout<<ans<<endl;
		
		
	}
}
