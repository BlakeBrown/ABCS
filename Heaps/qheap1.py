import heapq

heap = []
deleteList = set()

Q = input()
for i in range(0, int(Q)):
    line = input()
    operation = int(line[0])
    if operation == 1:
        a, b = line.split()
        heapq.heappush(heap, int(b))
    elif operation == 2:
        a, b = line.split()
        deleteList.add(int(b))
    elif operation == 3:
      while heap[0] in deleteList:
        deleteList.remove(heap[0])
        heapq.heappop(heap)
      print(heap[0])
        
    