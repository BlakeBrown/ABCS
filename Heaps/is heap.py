import math

isHeap = True

array = list(map(int, input().split()))
for i in range(1, len(array)):
    root = math.ceil(float(i)/2) - 1
    if array[i] < array[root]:
        isHeap = False
        break
if isHeap:
    print("true")
else:
    print("false")