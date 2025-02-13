import heapq
def kthLargest(matrix, k): # time O(n⋅m+n⋅mlog(n⋅m) and space O(n⋅m)
	#flat_array = [element for row in matrix for element in row] List comperhensive
	flat_array =[]
	for row in matrix:
		for element in row:
			flat_array.append(element)

	flat_array.sort()
	return flat_array[len(flat_array) - k]

#Use a Min-Heap 	time O(n⋅m⋅logk) space O(k)
def kthLargestUsingHeap(matrix, k):
	min_heap = []
	for row in matrix:
		for element in row:
			heapq.heappush(min_heap, element)
			if len((min_heap)) > k:
				heapq.heappop(min_heap)
	return heapq.heappop(min_heap)
# for smallest kth
def kthSmallestUsingHeap(matrix, k):
	max_heap = []
	for row in matrix:
		for element in row:
			heapq.heappush(max_heap, -element) ## Push negative values for max-heap
			if len((max_heap)) > k:
				heapq.heappop(max_heap)
	return -heapq.heappop(max_heap) # Return the root of the heap

matrix = [
	[10, 15, 25],
	[3,1,8],
	[9, 4, 9]
]
print(kthLargestUsingHeap(matrix, 3))
