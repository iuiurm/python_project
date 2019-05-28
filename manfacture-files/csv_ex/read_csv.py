# read-csv. py


with open('lunch.csv','r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for liner in lines:
        print(liner.strip().split(','))

#2 csv reader 사용하기
import csv

with open('lunch.csv','r', encoding = 'utf-8') as f:
    items = csv.reader(f)
    #reader 쓰는게 더 편한거 같음.
    for item in items :
        print(item)
