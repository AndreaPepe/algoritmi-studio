def selectionSort(a):
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:     #operazione dominante!!!
                min=j

        if min!=i:
            temp=a[i]
            a[i]=a[min]
            a[min]=temp
        #print(a)
array=[5,8,7,2,9,4,1,6,3]
selectionSort(array)
print(array)
