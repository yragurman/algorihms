import csv

def readerCSV(nameFile,columnNumber):
    Content = []
    with open (nameFile,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            Content.append(line[columnNumber])
    return Content