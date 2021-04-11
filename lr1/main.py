from readCSV import readerCSV
from Park import Park
from insertionSort import insertionSort
from heapSort import heapSort

ParkData = Park(readerCSV("Park.csv",0,False),readerCSV("Park.csv",1,True),readerCSV("Park.csv",2,True))

print("Sorted List:", *insertionSort(ParkData.bicyclePathLength))
print()
print("Sorted List:", *heapSort(ParkData.entryPrice))
