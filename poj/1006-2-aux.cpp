#include <iostream>
using namespace std;

void print(int mod,int remain);

int main(){
	print(28,5);
	print(23,4);
	return 0;
}

void print(int mod,int remain)
{
	int i,t,count;
	int a[50];
	for(i=0;i<mod;i++){
		t = i;
		count = 0;
		while(t%mod!=0){
			t += remain;
			count++;
		}
		a[i]=count;
	}
	for(i=0;i<mod;i++){
		cout << a[i] << ",";
	}
	cout << endl;
	return;
}
