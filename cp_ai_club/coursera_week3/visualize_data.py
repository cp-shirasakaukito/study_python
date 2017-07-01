import csv
import numpy as np
import matplotlib.pyplot as plt

#　データを読み込む
with open("ex2data1.txt",'r',newline='') as csvfile:
    read_csv = csv.reader(csvfile)
    y_exam1 = []
    y_exam2 = []
    n_exam1 = []
    n_exam2 = []
    for row in read_csv:
        if(row[2] == '1'):
            y_exam1.append(row[0])
            y_exam2.append(row[1])
        elif(row[2] == '0'):
            n_exam1.append(row[0])
            n_exam2.append(row[1])

# generate data

plt.scatter(y_exam1,y_exam2,c='green', marker='o')
plt.scatter(n_exam1,n_exam2,c='red',marker='x')
plt.title('Exam result',)
plt.xlabel('exam1')
plt.ylabel('exam2')
plt.show()