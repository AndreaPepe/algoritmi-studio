def partition(a,low,high):
    pivot=a[(low+high)//2]
    while True:
        i=low
        j=high
        while a[i]<pivot:
            i=i+1
        while a[j]>pivot:
            j=j-1
        if i>=j:
            return j
        temp=a[i]
        a[i]=a[j]
        a[j]=temp


def quickSort(a,low,high):
    if low<high:
        p=partition(a,low,high)
        quickSort(a,low,p)
        quickSort(a,p+1,high)



array=[23,45,3,46,7,77,82,35]
quickSort(array,0,len(array)-1)
print (array)
