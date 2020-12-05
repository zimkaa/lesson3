import csv
import json
from geopy import distance

streets = {}
with open("data-398-2020-12-02.csv", "r", encoding='cp1251') as file:
    data = csv.DictReader(file, delimiter=';')
    for row in data:
        if row['Street'] in streets:
            streets[row['Street']] += 1
        else:
            streets[row['Street']] = 1

# print(sorted(streets.items(), key=lambda item: item[1], reverse=True))

# RepairOfEscalators
with open("data-397-2020-11-16.json", "r", encoding='cp1251') as file:
    data = file.read()


data = json.loads(data)


# for line in data:
#     try:
#         if line["RepairOfEscalators"]:
#             # print(line["NameOfStation"])
#             line["NameOfStation"]
#     except:
#         #  выводит сроки в которых ошибка
#         print(line)


# for line in data:
#     try:
#         if line["RepairOfEscalators"]:
#             # print(line["NameOfStation"])
#             print(line["Name"])
#     except:
#         # выводит сроки в которых ошибка
#         print(line)


newport_ri = (55.89142924, 37.55729147)
cleveland_oh = (55.89460802, 37.55724554)

for 


dist_between = 
if (distance.distance(newport_ri, cleveland_oh).km)




# print(data[-2])
# print(data[-1])