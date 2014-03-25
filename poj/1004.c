#include <iostream>
using namespace std;

int main(){
	float ball,sum=0;
	int count=0;
	while(cin>>ball){
		sum += ball;
		count++;
	}
	cout << "$" << sum / count << endl;
	return 0;
}
