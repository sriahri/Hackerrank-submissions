#include <sstream>
#include <vector>
#include <iostream>
#include<string.h>
using namespace std;

int parseInts(string str) {
	// Complete this function
    int i;
    for(i=0;i<str.size();i++)
    {
        if(str[i]==',')
        {
            cout<<'\n';
        }
        else
        {
            cout<<str[i];
        }
    }
    return 0;
}

int main() {
    string str;
    cin >> str;
int integers = parseInts(str);
    return 0;
}