import csv
import random
from dataclasses import dataclass

@dataclass
class Student:
    firstName: str
    lastName: str
    tableAssigned: str


tables = []
studentArray = []

def tableAssignment(nStudent = int):
    tableNumber = 1
    for x in range(0,nStudent): 
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
    random.shuffle(tables)

 
  
with open('Dinner Seating - Student List 2018-19.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1
    tableAssignment(nStudent = line_count)
    line_count = 0
    for row in csv_reader: 
            studentArray.append(Student(row[1],row[0],tables[line_count]))
            line_count += 1
print(studentArray)




