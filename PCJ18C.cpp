#include<bits/stdc++.h>
using namespace std;

int gcd(int a,int b){
	if(a == 0) return b;
	else return(gcd(b % a, a));
}

int main(){
	ios_base::sync_with_stdio(false);
	int t, n, a, k;
	
	cin>>t;
	while(t--){
		cin>>n>>a>>k;
		
		int diff_nmr = ((n - 2) * 360 - 2* a * n);
		int diff_dnr = n * n - n;
		
		int ans_nmr = a * diff_dnr + (k - 1) * diff_nmr;
		int ans_dnr = diff_dnr;
		
		int g = gcd(ans_nmr, ans_dnr);
		ans_nmr/= g;
		ans_dnr /= g;
		cout<<ans_nmr<<" "<<ans_dnr<<"\n";
		
	}
}
