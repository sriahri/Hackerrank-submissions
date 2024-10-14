#include<typeinfo>
template <typename T> struct Traits
{
    static string name(int i)
    {
        string s=typeid(T).name();
        string sC[3]={"red", "green", "orange"};
        string sF[3]={"apple", "orange", "pear"};
        if(s.compare("5Color")==0)
        {
            if(i<3 && i>=0)
                return sC[i];
            else
                return "unknown";
        }else{
            if(i<3 && i>=0)
                return sF[i];
            else
                return "unknown";
        }
    }
};