import csv
import matplotlib
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

i = 0
with open("BitcoinHistoricalData.csv","r") as csv_file:
    for row in reversed(list(csv.reader(csv_file))):
        list = open("BitcoinHistoricalData.txt",'a')
        list.write(' ,'.join(row))
        list.write('\n')
        i=i+1
		
    
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)


def convertTuple(tup):
	str = ' '.join(tup)
	return str

x = []
y = []
for line in open('BitcoinHistoricalData.txt', 'r'):
    lines = [i for i in line.split()]
    data_lines = lines[0],lines[1],lines[2]
    x.append(convertTuple(data_lines))
    y.append(lines[4])

print(x) #Date
print(y) #price index


#Trading Strategy


#
#
#




