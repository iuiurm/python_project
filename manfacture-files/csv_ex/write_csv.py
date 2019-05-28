lunch = {
    '20층' : '123-345',
    '백수산' : '242-999',
    '양자강' : '1113-554'
}

with open('lunch.csv','w', encoding = 'utf-8') as f:
    for item in lunch.items() :   # ktems 는 key, value 갈 list 형태로 주어짐.
        f.write(f'{item[0]},{item[1]}\n')

with open('lunch2.csv','w', encoding='utf-8') as f :
    for item in lunch.items():
        f.write(' ,'.join(item) + '\n')

# 3. csv.writer
import csv
with open('lunch3.csv', 'w',encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items() :
        csv_writer.writerow(item)