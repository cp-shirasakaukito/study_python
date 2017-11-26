import matplotlib.pyplot as plt
from cp_ai_club.coursera_week3 import load_csv as csv
import os
#スクリプトのあるディレクトリの絶対パスを取得
name = os.path.dirname(os.path.abspath(__name__))

#絶対パスと相対パスをくっつける
joined_path = os.path.join(name, 'data/ex2data1.txt')

#正規化して絶対パスにする
data_path = os.path.normpath(joined_path)

#CSVデータを読み込む
data = csv.csv_handler(data_path)
#配列化する
grouped_data = data.divide_data_by_group(2)

# データを描画
plt.scatter(grouped_data['admitted']['exam1_score'],grouped_data['admitted']['exam2_score'],c='green', marker='o')
plt.scatter(grouped_data['not_admitted']['exam1_score'],grouped_data['not_admitted']['exam2_score'],c='red',marker='x')
plt.title('Exam result',)
plt.xlabel('exam1')
plt.ylabel('exam2')
plt.show()