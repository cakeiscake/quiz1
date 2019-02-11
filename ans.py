import json

def readcurrency(filename):
    data = []
    with open(filename, 'r') as fileobj:
        for line in fileobj:
            data.append({
                'symbol': line[0:3],
                'rate' : line[4:12]
            })

    return data

def printer(file):
    for line in file:
        print(line)

printer(readcurrency('currency.txt'))