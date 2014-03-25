#include <iostream>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

vector< pair<int,int> > input;

class MaxCounter {
public:
	MaxCounter(){
		pointer = 0;
		output.clear();
	};
	void init(){
		pointer = 0;
		output.clear();
	};
	void push_max(int max_value,int count){
		if(output.empty()){
			output.push_back(make_pair(max_value,count));
		} else if (count==0) {
			return;
		} else {
			if(output[pointer].first==max_value){
				output[pointer].second += count;
			} else {
				output.push_back(make_pair(max_value,count));
				pointer++;
			}
		}
		return;
	};
	void pop_result(){
		for(int p=0;p<=pointer;p++){
			cout << output[p].first << " " << output[p].second << endl;
		}
		cout << 0 << " " << 0 << endl;
		return;
	};
	bool have_element;
	int pointer;
	vector< pair<int,int> > output;
};

class Counter {
	public:
		Counter(){
			pointer = -1;
			count = 0;
		}
		Counter(int a){
			pointer = -1;
			count = a; 
		}
		void next(){
			if(count==0){
				pointer++;
				count = input[pointer].second - 1;
			} else {
				count--;
			}
			return;
		}
		void next(int jump){
			if(jump==1){
				next();
			} else if( jump > 1 ){
				if((count+1)>jump){
					count -= jump;
				} else {
					jump = jump - count - 1;
					count = 0;
					next();
					next(jump);
				}
			}
			return;
		}
		int value(){
			return input[pointer].first;
		}
		int pointer;
		int count;
};

int get_max(int a,int b,int c){
	return max( abs(a-b), abs(a-c) ); 
};

int get_max(int a,int b, int c,int d){
	return max( get_max(a,b,c), abs(a-d) );
};

int get_max(int a,int b, int c, int d, int e, int f){
	return max( get_max(a,b,c,d), get_max(a,e,f));
};

int main(){
	int width,value,length;
	int pixels;
	int pairs;
	//vector<pair<int,int>> input;
	while(cin>>width) {
		if(width==0){
			cout << 0 << endl;
			break;
		}
		pixels = 0;
		pairs = 0; 
		input.clear();
		//get input
		while(cin >> value >> length){
			if(value==0&&length==0){
				break;
			} else {
				input.push_back(make_pair<int,int>(value,length));
				pixels += length;
				pairs++;
			}
		}
		//start output
		cout << width << endl;

		if(width==1||width==pixels){//one col one row
			if(pairs==1){
				cout << 0 << " " << pixels << endl;
				cout << 0 << " " << 0 << endl;
			} else {
				int p;
				int cm = 0;
				MaxCounter mc;
				mc.init();
				if(input[0].second>1){
					mc.push_max(0,input[0].second-1);
					mc.push_max(abs(input[0].first-input[1].first),1);
				} else {
					mc.push_max(abs(input[0].first-input[1].first),1);
				}
				for(p=1;p<pairs-1;p++){
					if (input[p].second==1) {
						cm = get_max(input[p].first,input[p-1].first,input[p+1].first);
						mc.push_max(cm,1);
					} else {
						cm = abs(input[p].first-input[p-1].first);
						mc.push_max(cm,1);
						mc.push_max(0,input[p].second-2);
						cm = abs(input[p].first-input[p+1].first);
						mc.push_max(cm,1);
					}
				}
				//last
				mc.push_max(abs(input[p].first-input[p-1].first),1);
				mc.push_max(0,input[p].second-1);
				//how
				/*
				int p;
				int cm = 0;
				int cc = 0;
				int m;
				for(p=0;p<pairs-2;p++){
					m = input[p].first - input[p+1].first;
					if(m==cm){
						cc += input[p].second;
					}
				}
				*/
				//wront anwser1
				// for(p=0;p<pairs-2;p++){
				// 	if(input[p].first==input[p+1].first){
				// 		cm += input[p].second;
				// 	} else {
				// 		cout << 0 << " " << cm + input[p].second - 2 << endl;
				// 		cm = 0;
				// 		cout << abs(input[p].first-input[p+1].first) << " " << 2 << endl;
				// 	}
				// }
				// if(input[p].first==input[p+1].first){
				// 	cout << 0 << " " << cm + input[p].second + input[p+1].second << endl;
				// } else {
				// 	cout << 0 << " " << cm + input[p].second - 2 << endl;
				// 	cout << abs(input[p].first-input[p+1].first) << " " << 2 << endl;
				// 	cout << 0 << " " << input[p+1].second - 2 << endl;
				// }
				mc.pop_result();
			}			
			continue;
		}
		
		Counter u,ur;
		Counter ul(1);
		Counter l,m,r;
		Counter dl,d,dr;
		int store_max,count;
		int current_max;
		//init
		m.next();
		r.next(2);
		dl.next(width);
		d.next(width+1);
		dr.next(width+2);
		//item-1:
		store_max = get_max(m.value(),d.value(),r.value(),dr.value());
		count = 1;
		//item-2~width-1
		for(int i=0;i<width-2;i++){
			l.next();
			m.next();
			r.next();
			dl.next();
			d.next();
			dr.next();
			current_max = get_max(m.value(),l.value(),r.value(),dl.value(),d.value(),dr.value());
			if(current_max==store_max){
				count++;
			} else {
				cout << store_max << " " << count << endl;
				store_max = current_max;
				count = 1;
			}
		}
		//item-width
		l.next();
		m.next();
		r.next();
		dl.next();
		d.next();
		dr.next();
		current_max = get_max(m.value(),l.value(),dl.value(),d.value());
		if(current_max==store_max){
			count++;
		} else {
			cout << store_max << " " << count << endl;
			store_max = current_max;
			count = 1;
		}
		//item-width+1~pixels-width
		ur.next();
		for(int i=1;i<pixels-2*width+1;i++){
			ul.next();
			u.next();
			ur.next();
			l.next();
			m.next();
			r.next();
			dl.next();
			d.next();
			dr.next();
			//jump!
			if((input[m.pointer].second-m.count-1)>width && m.count>(width+1)){
				int jump = input[m.pointer].second - 2 * width - 2;
				/*if(jump>(pixels-i-2*width)){
					jump = pixels - 2 * width - i + 2;
					i = pixels - 2 * width;
				} else {
					i = i + jump;
				}*/
				i = i + jump;
				ul.next(jump);
				u.next(jump);
				ur.next(jump);
				l.next(jump);
				m.next(jump);
				r.next(jump);
				dl.next(jump);
				d.next(jump);
				dr.next(jump);
				if(store_max==0){
					count += jump + 1;
				} else {
					cout << store_max << " " << count << endl;
					store_max = 0;
					count = jump + 1;
				}
				continue;				
			}
			
			//left-item
			if(i%width==1){
				current_max = get_max(m.value(),ur.value(),r.value(),dr.value(),u.value(),d.value());
			} 
			//right-item
			else if(i%width==0){
				current_max = get_max(m.value(),ul.value(),l.value(),dl.value(),u.value(),d.value());
			} 
			//normal-item
			else {
				current_max = max(get_max(m.value(),ul.value(),l.value(),dl.value(),u.value(),d.value()),get_max(m.value(),ur.value(),r.value(),dr.value()));
			}
			if(current_max==store_max){
				count++;
			} else {
				cout << store_max << " " << count << endl;
				store_max = current_max;
				count = 1;
			}
		}
		//last-line
		ul.next();
		u.next();
		ur.next();
		l.next();
		m.next();
		r.next();
		current_max = get_max(m.value(),u.value(),ur.value(),r.value());
		if(current_max==store_max){
			count++;
		} else {
			cout << store_max << " " << count << endl;
			store_max = current_max;
			count = 1;
		}
		for(int i=0;i<width-2;i++){
			ul.next();
			u.next();
			ur.next();
			l.next();
			m.next();
			r.next();
			current_max = get_max(m.value(),ur.value(),r.value(),u.value(),l.value(),ul.value());
			if(current_max==store_max){
				count++;
			} else {
				cout << store_max << " " << count << endl;
				store_max = current_max;
				count = 1;
			}
		}
		//last-item
		ul.next();
		u.next();
		l.next();
		m.next();
		current_max = get_max(m.value(),u.value(),ul.value(),l.value());
		if(current_max==store_max){
			count++;
		} else {
			cout << store_max << " " << count << endl;
			store_max = current_max;
			count = 1;
		}
		cout << store_max << " " << count << endl;
		cout << 0 << " " << 0 << endl;
	}
	return 0;
}
