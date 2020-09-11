def insertionSort(array):
    n = len(array)
    for i in range(1,n):
        key=array[i]
        j=i-1
        while (j>=0 and array[j]>key):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key


def bucketSort(a,k):
    buckets=[]
    for i in range(k):
        buckets.append([])

    max=a[0]
    for i in range(1,len(a)):
        if a[i]>max:
            max=a[i]

    for i in range(len(a)):
        buckets[(k*a[i])//(max+1)].append(a[i])
    print(buckets)
    for i in range(k):
        insertionSort(buckets[i])
    print(buckets)


    index=0
    for i in range(len(buckets)):
        n=len(buckets[i])
        for j in range(n):
            a[index]=buckets[i][j]
            index += 1
    #print(a)


array=[23,45,3,46,7,77,82,35]
bucketSort(array,4)
print (array)
