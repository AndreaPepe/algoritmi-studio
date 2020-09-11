#!/usr/bin/env python3

from dynamic_Array import dynamicArray

arr = dynamicArray()
print("The array is large", len(arr))

arr.append("some string")
arr.append(10)
arr.append([1,2,3])

print("The array is large", len(arr))

print("Element at 1 is:", arr[1])
print("Element at 2 is:", arr[2])

print("Element 10 has been stored in Dynamic Array:", 10 in arr)

for element in arr:
    print(element)
