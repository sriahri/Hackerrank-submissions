#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int i,n,p;
    cin>>n;
    cin>>p;
    for(i=n;i<=p;i++)
    {
        if(i>9)
        {
            if(i%2==0)
                cout<<"even\n";
            else
                cout<<"odd\n";
        }
        else
        {
            if(i==1)
                cout<<"one\n";
            else if(i==2)
                cout<<"two\n";
            else if(i==3)
                cout<<"three\n";
            else if(i==4)
                cout<<"four\n";
            else if(i==5)
                cout<<"five\n";
            else if(i==6)
                cout<<"six\n";
            else if(i==7)
                cout<<"seven\n";
            else if(i==8)
                cout<<"eight\n";
            else if(i==9)
                cout<<"nine\n";
                
        }
    }
    return 0;
}