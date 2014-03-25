#include <iostream>
using namespace std;

int main(){
	int p,e,i,d;
	int count=0;
	int day;
	while(true){
		cin >> p >> e >> i >> d;
		if( p == -1 && e == -1 && i == -1 && d == -1){
			break;
		}
		count++;

		day = d - i + 1;
		while((day%33)!=0){
			day++;
		}
		
		day = day + i - e;
		while((day%28)!=0&&(day-d)<21252){
			day = day + 33;
		}
		
		day = day + e - p;
		while((day%23)!=0&&(day-d)<21252){
			day = day + 924;
		}

		if((day-d)>21252){
			day = 21252 - d;
		} else {
			day = day - d + p;
		}
		cout << "Case "<< count << ": the next triple peak occurs in " << day << " days." << endl;
	}
	return 0;
}
