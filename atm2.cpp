#include<bits/stdc++.h>
using namespace std;

int main(){
	int t, n, k;
	cin>>t;
	while(t--){
		string ans;
		cin>>n>>k;
		int a;
		for(int i = 0; i < n; i++) 
		{
			cin>>a;
			if(k - a >= 0)
			{
			
				k -= a;
				ans += '1';
			}
			else
				ans += '0';
		}
		cout<<ans<<"\n";
		
	}
}
