#include <bits/stdc++.h>
using namespace std;

int main(){
	
	int t;
	double h,s,a_plus_b,a_minus_b,a,b;
	cin>>t;
	while(t--){
		cin>>h>>s;
		a_plus_b = sqrt(h * h + 4 * s);
		a_minus_b = sqrt(h * h - 4 * s);
		
		a = (a_plus_b + a_minus_b) / 2;
		b = (a_plus_b - a_minus_b) / 2;
		if(a>0 && b>0)
        {
            if(b>a)
            	swap(a, b);
        printf("%0.6lf %0.6lf %0.6lf\n",b,a,h);
        //cout<<b<<a<<h<<endl;
        }
        else
        	cout<<-1<<endl;
		
	}
}
