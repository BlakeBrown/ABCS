#!/bin/python3

import os
import sys
import heapq

#
# Complete the minimumAverage function below.
#
def minimumAverage(customers):
  heapq.heapify(customers)

  N = len(customers)
  pizzas = []
  time = 0
  totalWaitingTime = 0

  while len(customers) > 0 or len(pizzas) > 0:
    while len(customers) > 0 and customers[0][0] <= time:
      heapq.heappush(pizzas, [customers[0][1], customers[0][0]])
      heapq.heappop(customers)
    if len(pizzas) == 0:
      time = customers[0][0]
      continue
    # Cook pizza
    pizza = heapq.heappop(pizzas)
    totalWaitingTime += (time + pizza[0] - pizza[1])
    time += pizza[0]
  return int(totalWaitingTime / N)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
