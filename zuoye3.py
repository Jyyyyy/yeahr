import csv 
import re 
path='C:\\Users\\简影\\Desktop\\un-general-debates\\un-general-debates.csv'
with open(path,mode='r',encoding='utf-8') as f:
    csv_reader=csv.reader(f)
# print(csv_reader)
    for row in csv_reader:
        q=row[3]
        path_='C:/Users/简影/Desktop/jy.txt'
        with open(path_,'w',encoding='utf-8') as ro: 
            ro.write(q)