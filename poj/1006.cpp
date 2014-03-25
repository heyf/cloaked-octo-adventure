#include <iostream>
using namespace std;

int main(){
	int p,e,i,d = 0;
	int dp,de,di;
	int count=0;
	int days= 0;
	while(true){
		cin >> p >> e >> i >> d;
		if( p == -1 && e == -1 && i == -1 && d == -1){
			break;
		}
		count++;
		dp = d - p + 1;
		di = d - i + 1;
		de = d - e + 1;
		for(days=1;days<21252;days++){
			if(dp%23==0&&de%28==0&&di%33==0) {
				break;
			}
			dp++;de++;di++;		
		}
		cout << "Case "<< count << ": the next triple peak occurs in " << days << " days." << endl;
	}
	return 0;
}
