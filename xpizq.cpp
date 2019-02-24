#include<bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
	if(a == 0)
		return b;
	else
		return(gcd(b % a, a));
}
int main(){
	int t;
	cin>>t;
	while(t--){
		ios_base::sync_with_stdio(0);
		long long n, typ, x, y, z;
		cin>>n>>typ>>x>>y>>z;
		long long nmr = 0;
		long long dnr = 2 * n + 1;
		
		if(typ == 1){
			if(z == x)
				nmr = z;
			else
				nmr = dnr - z;		
		}
		else if(typ == 4)
			nmr = dnr - 2*y;
		else if(typ == 2){
			nmr = dnr  - 2*y;
		}
		else if(typ == 3){
			if(z == x)
				nmr = x;
			else
				nmr = dnr - x;
		}
		
		long long g = gcd(nmr, dnr);
		cout<<nmr/g<<" "<<dnr/g<<endl;
	
	}
}
