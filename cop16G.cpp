#include<iostream>
using namespace std;
typedef long long int ll;
ll gcd(ll a,ll b)
{
	if(a==0)
		return b;
	else 
		return gcd(b%a,a);
}
int main()
{
	int t;
	cin>>t;
	ll a,b;
	while(t--)
	{
		scanf("%lld%lld",&a,&b);
		if(gcd(a,b)!=1)
			cout<<"-1\n";
		else 
			printf("%lld\n",a*b-a-b+1);

	}
}
