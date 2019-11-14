from collections import defaultdict

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

hashtable = defaultdict(int)
for e in A:
    hashtable[e] += 1

ans = 0
for j in range(0, len(B)):
    for k in range(0, len(C)):
        for l in range(0, len(D)):
            requiredValue = -B[j] - C[k] - D[l]
            if requiredValue in hashtable:
                ans += hashtable[requiredValue]
print(ans)