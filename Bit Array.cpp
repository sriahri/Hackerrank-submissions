#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
using namespace std;
bitset<536870912>p;
bitset<536870912>q;
bitset<536870912>r;
bitset<536870912>s;
int main() {
    unsigned int S;
    unsigned long long N,P,Q;
    cin>>N>>S>>P>>Q;
    if(S<536870912){
        p.set(S);
    }
    else if(S<1073741824){
        q.set(S-536870912);
    }
    else if(S<1610612736){
        r.set(S-1073741824);
    }
    else{
        s.set(S-1610612736);
    }
    for(int i=1;i<N;i++){
        S=((S*P+Q)&2147483647);
        if(S<536870912){
            p.set(S);
        }
        else if(S<1073741824){
            q.set(S-536870912);
        }
        else if(S<1610612736){
            r.set(S-1073741824);
        }
        else{
            s.set(S-1610612736);
        }
    }
    cout<<p.count()+q.count()+r.count()+s.count();
    return 0;
}