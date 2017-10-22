import csv
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


class csv_handler():
    def __init__(self,file_name):
        self.data = np.loadtxt(file_name,delimiter=",")

    # 読み込んだデータをグループ化する
    # 前提：group化されるキーは負の整数0からの連番で表現される
    def divide_data_by_group(self,group_key_col_num):
        #空の辞書データを作成
        group_data_set= dict()
        group_data_set['admitted'] = dict()
        group_data_set['not_admitted'] = dict()
        group_data_set['admitted']['exam1_score'] = []
        group_data_set['admitted']['exam2_score'] = []
        group_data_set['not_admitted']['exam1_score'] = []
        group_data_set['not_admitted']['exam2_score'] = []
        #空の辞書データにCSVの値を入れていく
        for row_data in self.data:
            if(row_data[group_key_col_num] == 1):
                group_data_set['admitted']['exam1_score'].append(row_data[0])
                group_data_set['admitted']['exam2_score'].append(row_data[1])
            else:
                group_data_set['not_admitted']['exam1_score'].append(row_data[0])
                group_data_set['not_admitted']['exam2_score'].append(row_data[1])

        return group_data_set

#CSVデータを読み込む
data = csv_handler('ex2data1.txt')
#配列化する
grouped_data = data.divide_data_by_group(2)

# データを描画
plt.scatter(grouped_data['admitted']['exam1_score'],grouped_data['admitted']['exam2_score'],c='green', marker='o')
plt.scatter(grouped_data['not_admitted']['exam1_score'],grouped_data['not_admitted']['exam2_score'],c='red',marker='x')
plt.title('Exam result',)
plt.xlabel('exam1')
plt.ylabel('exam2')
plt.show()