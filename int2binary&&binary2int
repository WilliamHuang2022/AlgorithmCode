#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

vector<int> int2binary(int n){
    int res=n;
    vector<int> ans;
    while (res!=0){
        ans.insert(ans.begin(),res%2);
        res=res/2;
    }
    return ans;
}

int binary2int(vector<int> vec){
    int len=vec.size();
    int sum=0,sumi=0;
    for(int i=0;i<len;i++){
        sumi=(int) pow(2,len-1-i);
        sum+=vec[i]*sumi;
    }

    return sum;
}
