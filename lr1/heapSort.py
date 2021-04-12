import algorithmOperation
import time


def maxHeapify (List,heapSize,currentNumberIndex):
    maxValueIndex = currentNumberIndex
    leftChildIndex = currentNumberIndex * 2 + 1
    rightChildIndex = currentNumberIndex * 2 + 2

    if leftChildIndex < heapSize and List[leftChildIndex] > List[maxValueIndex]:
        maxValueIndex = leftChildIndex
        algorithmOperation.comparisonCountHeapSort += 2

    if rightChildIndex < heapSize and List[rightChildIndex] > List[maxValueIndex]:
        maxValueIndex = rightChildIndex
        algorithmOperation.comparisonCountHeapSort += 2

    if maxValueIndex != currentNumberIndex:
        algorithmOperation.swap(List,currentNumberIndex,maxValueIndex)
        algorithmOperation.comparisonCountHeapSort += 1
        algorithmOperation.swapCountHeapSort += 1
        maxHeapify(List,heapSize,maxValueIndex)
  

def buildMaxHeap(List,heapSize):
    for currentNumberIndex in range(heapSize//2-1, -1, -1):
        maxHeapify(List,heapSize,currentNumberIndex)

def heapSort(List):
    Start = time.perf_counter()
    print("Heapsort:")
    heapSize = len(List)
    buildMaxHeap(List,heapSize)
    for iteration in range(heapSize-1,0,-1):
        algorithmOperation.swap(List,iteration,0)
        algorithmOperation.swapCountHeapSort += 1
        maxHeapify(List,iteration,0)
    print("Count of swaps:", algorithmOperation.swapCountHeapSort)
    print("Count of comparisons:", algorithmOperation.comparisonCountHeapSort)
    End = time.perf_counter()
    print(f"Time wasted to sort list by Heap sort = {End - Start:0.10f} seconds")
    return List


arr = [5,1,3,8,2,5,3,9,2]
print(heapSort(arr))


