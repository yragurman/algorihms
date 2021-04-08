from readCSV import readerCSV
from Park import Park
from insertionSort import insertionSort

ParkData = Park(readerCSV("Park.csv",0),readerCSV("Park.csv",1),readerCSV("Park.csv",2))

print(*insertionSort(ParkData.bicyclePathLength), sep=', ')
