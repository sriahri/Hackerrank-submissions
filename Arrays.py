

def arrays(arr):
    # complete this function
    # use numpy.array
    l=[]
    for i in arr[::-1]:
        l.append(float(i))
    array=numpy.array(l)
    return array

