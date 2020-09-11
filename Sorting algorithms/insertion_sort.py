def insertionSort(array):
    n = len(array)
    for i in range(1,n):
        key=array[i]
        j=i-1
        while (j>=0 and array[j]>key):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
        print(array)

a=[9,8,7,6,5,4,3,2,1]
b=[2,6,4,8,7,3,1,9,5]
c=[1,2,3,4,5,6,7,8,9]
d=[15,20,10,18]
insertionSort(d)        # to prove with a,b or c
print(d)
