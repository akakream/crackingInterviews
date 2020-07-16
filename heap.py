from heapq import heappush, heappop, heapify

heap = []

nums = [3,56,42,9,5,78,4,28,6,7,3,69,3,74,62,0]

for item in nums:
    heappush(heap, item)

ordered = []
while heap:
    ordered.append(heappop(heap))

print(ordered)
