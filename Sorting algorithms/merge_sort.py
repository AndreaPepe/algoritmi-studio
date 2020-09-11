def merge(a,left,center,right):
    b=[]
    for i in range(len(a)):
        b.append(a[i])
    i=left
    j=center+1
    k=left

    while (i<=center and j<=right):
        if (a[i]<=a[j]):
            b[k]=a[i]
            i=i+1
        else:
            b[k]=a[j]
            j=j+1
        k=k+1
    #print(b)
    j=right
    h=center
    while h>=i:
        a[j]=a[h]
        j=j-1
        h=h-1
    for x in range(left,k):
        a[x]=b[x]
    print(a)



def mergeSort(a,left,right):
    if left<right:
        center = (left+right)//2
        mergeSort(a,left,center)
        mergeSort(a,center+1,right)
        merge(a,left,center,right)

array=[5,8,7,2,9,4,1,6,3]
mergeSort(array,0,len(array)-1)
print(array)
