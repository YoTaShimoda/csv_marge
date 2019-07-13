import csv
import math
import helper

with open('no5__2017-12-06_08-25-28.csv') as f:
    reader = csv.reader(f)
    list = [row for row in reader]  # リスト型に変換している
    start_time = list[1][3]
    start_time_second = start_time[-2:]
    start_time_minute = start_time[3:5]
    start_time_hour = start_time[:2]
    load_start_second = 60-int(start_time_second)
    read_data = {}

    for i in range(4,70):              #開始位置決定用
        time_value = list[i][1]
        time_value_second = int(time_value[-2:])
        if time_value_second == load_start_second :
            if list[i][2] == None:                              # 後でNoneなのかゼロなのか聞く
                load_start_index_value = i+60
            else:
                load_start_index_value = i
            break

    load_start_index_value = int(load_start_index_value) #ここでの-1は、配列が0から数え始めるため
    count = 0                # 実行回数決定用
    for row in list:
        count += 1
    count = count-3-load_start_index_value
    count = math.floor(count / 60)
    count_total = 0
    count_write = 0     #ここまでーーーーーーーーーーーーーーーーーー〜〜〜ー
    value_sum = 0
    for i in range(0,count):
        for a in range(0,60):
            value = list[load_start_index_value][2]
            value_sum += int(value)
            load_start_index_value += 1
        average = math.floor(value_sum/60)
        time = list[load_start_index_value][1]

        try:
            hour = time[:2]
            hour = int(hour)+int(start_time_hour)
        except:
            hour = time[:1]
            hour = int(hour)+int(start_time_hour)

        minute = time[3:5]
        minute = int(minute)+int(start_time_minute)

        if minute > 59:       # 時間計算
            minute = minute - 60
            hour = int(hour) + 1
        if hour < 10:
            hour = '0' + str(hour)
        else:
            str(hour)

        if minute < 10:      #分が一桁だと、マッチしないので、05分という形に変換する。
            minute = '0'+ str(minute)
        else:
            minute = str(minute)

        read_data_index = helper.create_write_data(hour,minute)           # read_data(辞書型)に追加するフォーマットに変換
        read_data[read_data_index] = average
        value_sum = 0
    print(read_data)