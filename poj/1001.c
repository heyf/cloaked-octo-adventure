#include <iostream> 
using namespace std;
void main(){
	double sum;
	double s;
	int n;
	while(cin>>s>>n){
		sum = s;
		for(var i = 0; i < n-1;i++){
			sum = sum * s;	
		}
		cout << sum << endl; 
	}
}
