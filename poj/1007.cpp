#include <iostream>
#include <string>
using namespace std;

int main(){
	int n,m,i,j,k,count;
	string temp;
	string seq[100];
	int seq_sort[100];
	cin >> n >> m;
	for(i=0;i<m;i++){
		cin >> temp;
		count = 0;
		for(j=0;j<n-1;j++){
			for(k=j+1;k<n;k++){
				if(temp[j]>temp[k]){
					count++;
				}
			}
		}
		j=0;
		while(count>=seq_sort[j]&&j<i){
			j++;
		}
		for(k=i;k>j;k--){
			seq_sort[k]=seq_sort[k-1];
			seq[k]=seq[k-1];
		}
		seq[j]=temp;
		seq_sort[j]=count;	
	}

	for(j=0;j<m;j++){
		cout << seq[j] << endl;
	}
	return 0;
}
