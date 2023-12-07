import csv
import pandas as pd

def split(file):
    data_1, data_2, data_3 = [], [], []
    with open(file, 'r') as file:
        data_1 = file.read()
        data_1 = data_1.split('),')
        for line in data_1:
            if len(line) < 100:
                continue
            else:
                data_2.append(line.split(','))
    
    for line in data_2:
        dicti = {}
        if len(line) == 5:
            dicti['Пассажир'] = line[0]
            dicti['Маршрут'] = line[1]
            dicti['Мест'] = 1
            dicti['Остановка'] = line[2]
            dicti['Телефон'] = line[4]
            data_3.append(dicti)

        else:
            dicti['Пассажир'] = line[0]
            dicti['Маршрут'] = line[1]
            dicti['Мест'] = line[2]
            dicti['Остановка'] = line[3]
            dicti['Телефон'] = line[5]
            data_3.append(dicti)
    return data_3


with open('1end.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(("Пассажир", "Маршрут", "Мест","Остановка", "Телефон"))

        for line in data_3:
            writer.writerow((line["Пассажир"],line["Маршрут"],line["Мест"],line["Остановка"],line["Телефон"]))


# for line in data_3:
#     with open('1end.csv', 'a', encoding='utf-8') as new_file:
#         writer = csv.writer(new_file, fieldnames=fields)
#         writer.writerow(line)


if __name__ == '__main__':
    new_data = split('1end.txt')


