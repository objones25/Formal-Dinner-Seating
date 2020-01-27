import csv
import random

tables = []
tableNumber = 1

for x in range(0,290): 
    if x < 31:
        tables.append(str(tableNumber) + 'w')                   
        tableNumber +=1
    else:
        if tableNumber < 32:
            tables.append(str(tableNumber))                   
            tableNumber +=1
        else:
            tables.append('Kitchen Crew') 
            tableNumber = 1
# creates an array of table numbers. 
# first 31 in list are marked with w to denote waiter
# Table counter resets to 1 when table number reaches 32. 
# 32 is kitchen crew table.
random.shuffle(tables)
# List of tables are randomized
 
  
with open('Dinner Seating - Student List 2018-19.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            print(f'\t Last name: {row[0]}, First name: {row[1]}, Table#: {tables[line_count]}.')
            line_count += 1
# names are matched with randomized list of table numbers.
# list is printed line by line
