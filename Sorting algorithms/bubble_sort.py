def bubbleSort(a):
    n=len(a)
    swap=True

    while swap:
        swap=False
        for i in range(n-1):
            if a[i]>a[i+1]:
                temp=a[i]           # operazione DOMINANTE!!!
                a[i]=a[i+1]
                a[i+1]=temp
                swap=True
                #print(a)

array=[5,8,7,2,9,4,1,6,3]
bubbleSort(array)
print(array)
