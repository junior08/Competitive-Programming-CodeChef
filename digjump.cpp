#include <bits/stdc++.h>
using namespace std;

vector<vector<int> > v(100001);
string s;
bool check[10];
int ans[100001];
int n;

void bfs(){
	queue <int> q;
	int idx;
	q.push(0);
	
	while(!q.empty()){
		int i =  q.front();
		q.pop();
		
		if(i > 1 && !ans[i - 1]){
			ans[i - 1] = ans[i] + 1;
			q.push(i - 1);
		}
		if(i < n - 1 && !ans[i + 1]){
			ans[i + 1] = ans[i] + 1;
			q.push(i + 1);
		}
		
		int val = s[i] - '0';
		if(!check[val]){
			check[val] = true;
			for(int k = 0; k < v[val].size(); k ++){
				idx = v[val][k];
				if(!ans[idx] && idx!=0 && idx!=i)
    				{
    					ans[idx] = ans[i] + 1;
    					q.push(idx);
    				}
				
			}
		}
		
	}
	
}

int main()
    {
    	ios_base::sync_with_stdio(false);
    	cin>>s;
    	n = s.size();
    	
    	for(int i=0;i<10;i++)
    		check[i] = false;
    		
    	for(int i=0;i<n;i++)
    	{
    		v[s[i] - '0'].push_back(i);
    		ans[i] = 0;
    	}
    	bfs();
    	cout<<ans[n-1]<<"\n";
    	return 0;
    }  
