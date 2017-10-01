# f = open('animals.csv')

# for line in f:
#     print(line)

# f.close()

# with open('animals.csv', 'r') as f:
#     print(f.read())
    
# import csv
# with open('animals.csv', 'r') as f:
#     animals = csv.reader(f)
#     for row in animals:
#         if row[-1] == 'True':
#             print("{0} is a {1} and is housebroken".format(row[0], row[1]))
#         elif row[-1] == 'False':
#             print("{0} is a {1} and is not housebroken!".format(row[0], row[1]))

# import json
# with open('animals.json', 'r') as r:
#     data = json.load(r)
#     for row in data:
#         print(row['name'])

# f = open('cars.txt', 'a')
# cars = ['chevy', 'tesla', 'ford']
# for car in cars:
#     f.write(car + '\n')

# f.close()

# with open('cars.txt', 'a') as f:
#     cars = ['chevy', 'vw', 'mazda']
#     for car in cars:
#         f.write(car + '\n')

cars = [
    {"make": "chevy"},
    {"make": "tesla"},
    {"make": "porsche"}
]
import json
with open('cars.json', 'w') as f:
    json.dump(cars, f)