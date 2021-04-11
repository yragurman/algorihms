import csv

def readerCSV(nameFile,columnNumber,isNumber):
    Content = []
    with open (nameFile,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            Content.append(line[columnNumber])
    if isNumber:
        ConvertedContentToFloat = [float(number) for number in Content]
        return ConvertedContentToFloat
    else:
        return Content
