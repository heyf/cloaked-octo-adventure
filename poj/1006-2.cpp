#include <iostream>
using namespace std;

int main(){
	int p,e,i,d;
	int a[28]={0,11,22,5,16,27,10,21,4,15,26,9,20,3,14,25,8,19,2,13,24,7,18,1,12,23,6,17};
	int b[23]={0,17,11,5,22,16,10,4,21,15,9,3,20,14,8,2,19,13,7,1,18,12,6};
	int date,count=0;
	int remain;
	while(true){
		cin >> p >> e >> i >> d;
		if( p == -1 && e == -1 && i == -1 && d == -1){
			break;
		}
		count++;
		
		date = d;
		//step 1:
		remain = (d-i)%33;
		if(remain<0){
			remain += 33;
		}
		d = d + 33 - remain;
		
		//step 2:
		remain = (d-e) % 28;
		if(remain<0) {
			remain += 28;
		}
		d = d + 33 * a[remain];
		
		//step 3:
		remain = (d-p) % 23;
		if(remain<0) {
			remain += 23;
		}
		d = d + 33 * 28 * b[remain];

		//step 4:
		if(d>21617){
			d = 21252;
		} else {
			d = d - date;
		}
		
		cout << "Case "<< count << ": the next triple peak occurs in " << d << " days." << endl;
	}
	return 0;
}
