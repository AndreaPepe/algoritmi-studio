array=[-12,-8,-6,4,21,56,87,101,125,126]

def binSearch(a,low,high,value):
    if high<low:
        return None
    mid=(high+low)//2
    if a[mid] > value:
        return binSearch(a,low,mid-1,value)
    elif a[mid] < value:
        return binSearch(a,mid+1,high,value)
    else:
         return mid


print (binSearch(array,0,len(array)-1,12))
