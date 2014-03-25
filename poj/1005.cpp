#include <iostream>
using namespace std;

int main(){
	int n,count;
	int i;
	float area;
	float x,y;
	cin >> n;
	count = n;
	while(n>0){
		n--;
		cin >> x >> y;
		area = ( x * x + y * y ) * 3.1415 / 2.0;
		for(i=0;area>0;i++){
			area = area - 50;
		}
		cout << "Property " << count - n << ": This property will begin eroding in year " << i << "." << endl;
	}
	cout << "END OF OUTPUT." << endl;
	return 0;
}
