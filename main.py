import random
from collections import deque
def mergeSort(x):

    if len(x) <= 1:
        return x
    
    halfway = len(x)//2

    leftArray = mergeSort(x[:halfway])
    rightArray = mergeSort(x[halfway:])

    newArray = []

    left = deque(leftArray)
    right = deque(rightArray)

    while left and right:
        newArray.append(left.popleft() if left[0] <= right[0] else right.popleft())

    newArray.extend(right)
    newArray.extend(left)

    return newArray

newArray = []
length = int(input("Enter array size: "))

for i in range(length):
    newArray.append(i+1)

random.shuffle(newArray)

print("before sort:", newArray)

print("after sort:", mergeSort(newArray))