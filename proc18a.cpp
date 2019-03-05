#include<bits/stdc++.h>
using namespace std;

int main(){
	int t, n, k, a[105], from[105], sm, curr;
	cin>>t;
	while(t--){
		curr = -1;
		cin>>n>>k;
		for(int i = 0; i < n; i++)
			cin>>a[i];
		
		for(int i = 0; i < n ; i ++){
			sm = 0;
			for(int j = i; j < min(i + k, n); j++){
				sm += a[j];
			}
			from[i] = sm;
		}
		from[n - 1] = a[n - 1];
		for(int i = 0; i < n; i++){
			if(from[i] > curr){
				curr = from[i];
			}
		}
		cout<<curr<<"\n";
	}
}
