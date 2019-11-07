def cookies(k, A):
    h.heapify(A)
    count = 0
    
    while A[0] < k:
        if len(A) < 2: 
          return -1
    
        h.heappush(A, h.heappop(A) + h.heappop(A) * 2)
        count += 1
        
    return count