#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    int n1,n2,i;
    string s1,s2;
    char t;
    cin>>s1>>s2;
    cout<<s1.size()<<' '<<s2.size();
    cout<<'\n';
    cout<<s1<<s2<<'\n';
    t=s1[i];
    s1[0]=s2[0];
    s2[0]=t;
    cout<<s1<<' '<<s2;
    
    
  
    return 0;
}