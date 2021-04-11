import algorithmOperation
import time

def insertionSort (List):
    swapCount = 0
    comparisonCount = 0
    Start = time.perf_counter()
    print("Insertion sort:")
    for item in range(1, len(List)):
        valueToSort = List[item]
        while List[item-1] < valueToSort and item > 0:
            algorithmOperation.swap(List,item,item-1)
            swapCount += 1
            comparisonCount += 2
            item = item - 1
    print("Count of swaps:", swapCount)
    print("Count of comparisons:", comparisonCount)
    End = time.perf_counter()
    print(f"Time wasted to sort list by insertion sort = {End - Start:0.10f} seconds")
    return List