#include<bits/stdc++.h>
using namespace std;

int main(){
	long long n, m, a;
	cin>>n>>m>>a;
	long long ans;
	
	ans = (n / a + (n % a > 0))* (m / a + (m % a > 0));
	cout<<ans;
	
}
