array=[-12,-8,-6,4,21,56,87,101,125,126]

def binSearch(a,value):
    low=0
    high=len(a)-1

    while low <= high:
        mid = (low+high)//2
        if a[mid]>value:
            high=mid-1
        elif a[mid]<value:
            low=mid+1
        else:
            return mid
    return None


print (binSearch(array,56))
