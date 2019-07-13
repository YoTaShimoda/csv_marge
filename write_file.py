import csv
import read_file
file_name = 'no5-1METS_20171206.csv'
with open(file_name,encoding='cp932') as f:
    reader = csv.reader(f)
    list= [row for row in reader]
    leng = len(list)
    read_leng = len(read_file.read_data)
    for i in range(5,leng):   #総当たりでしかできていないので要改良
        if list[i][0] in read_file.read_data:
            list[i].append(read_file.read_data[list[i][0]])
    print(list)

write_file_name = file_name.replace('.csv','_marge_result.csv')
with open(write_file_name,'a',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(list)





