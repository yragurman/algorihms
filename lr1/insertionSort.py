def insertionSort (List):
    print("Insertion sort:")
    swapCount = 0
    comparisonCount = 0
    for item in range(1, len(List)):
        valueToSort = List[item]
        comparisonCount +=1
        while List[item-1] < valueToSort and item > 0:
            List[item], List[item-1] = List[item-1], List[item]
            swapCount += 1
            comparisonCount += 1
            item = item - 1
    print(swapCount)
    print(comparisonCount)
    return List