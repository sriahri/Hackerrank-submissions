// Enter your code for reversed_binary_value<bool...>()
template<bool...digits>
int reversed_binary_value()
{
    int i = 0, z=0, size = sizeof...(digits);
    bool d[size] = {digits...};
    for(int k = 0; k < size; k++){
        z += ((int) d[k]) << i++;
    }
    return z;
}