#include<bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	
	int t, n, ans;
	ans = 0;
	cin>>t;
	while(t--){
		int c = 1;
		ans = 0;
		cin>>n;
		for(int i = n; i >= 1; i --){
			if(i % 2){
				ans += c * c;
				
			}
			c += 1;
			
		}
		cout<<ans<<"\n";
	}
}
