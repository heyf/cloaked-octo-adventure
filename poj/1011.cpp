#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

class Sticks {
public:
	Sticks(){
		init();
	};
	vector< pair<int,int> > sticks;//value;count
	vector< pair<int,int> > calc;
	int size,sum;
	int osum;
	void init(){
		size = 0;
		sum = 0;
		sticks.clear();
	}
	void push(int value){
		sum += value;
		if( size == 0 ){
			add(value);
			return;
		} 
		for(int i=0;i<size;i++){
			if(sticks[i].first==value){
				sticks[i].second++;
				return;
			}
		}
		add(value);
		return;
	};
	void add(int value){
		sticks.push_back(make_pair(value,1));
		size++;
	};
	void finish_input(){
		sort(sticks.begin(),sticks.end());
		//dump(sticks);
		for(int i=sticks[size-1].first;i<=sum;i++){
			//bool result = false;
			if(sum%i==0){
				osum = i;
				calc = sticks;
				cout << "current: " << osum << endl;
				//dump(calc);
				if(dfs(size-1,0,0,sum/osum,true)){
					cout << i << endl;
					return;
				};
			}
		}
	};
	void dump(vector< pair<int,int> > v){
		for(int i=0;i<size;i++){
			cout << v[i].first << " " << v[i].second << endl;
		}
	};
	bool dfs(int i, int i_count, int csum, int ctimes,bool flag){
		//cout << i << " " << i_count << " " << csum << endl;
		if(ctimes==1){
			return true;
		}
		if(i<0){
			return false;
		}
		if(i_count>=calc[i].second){//sticks[i] is full
			return dfs(i-1,0,csum,ctimes,flag);
		}
		if(csum+sticks[i].first==osum){
			calc[i].second--;
			//cout << "find " << i << " " << i_count << " " << csum << endl;
			if(dfs(size-1,0,0,ctimes-1,true)){
				//cout << sticks[i].first << " = " << osum << endl;
				return true;
			}
			calc[i].second++;
			if(flag){
				return false;
			}			
			return dfs(i-1,0,csum,ctimes,flag);;
		} else if(csum+sticks[i].first<osum){
			calc[i].second--;
			if(dfs(i,i_count+1,csum+sticks[i].first,ctimes,false)){
				//cout << calc[i].first << " + ";
				return true;
			}
			calc[i].second++;
			if(flag){
				return false;
			}
			return dfs(i-1,0,csum,ctimes,flag);;			 
		} else {
			//cout << sticks[i].first << " > " << osum << endl;
			if(flag){
				return false;
			}
			return dfs(i-1,0,csum,ctimes,flag);
		}
	};
};

int main(){
	int flag,stick,sum;
	Sticks s;
	while(cin>>flag){
		if(flag==0){
			break;
		}
		s.init();
		for(int i=0;i<flag;i++){
			cin >> stick;
			s.push(stick);
		}
		s.finish_input();

		//s.dump(s.calc);
		//s.dump();
		//cout << s.sum << endl;
		// for(int i=0;i<flag;i++){
		// 	cout << sticks[i] << " ";
		// }
		// cout << endl;

	}
	return 0;
}