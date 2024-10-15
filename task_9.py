import csv
import json


csv_file_path = 'cars.csv'
json_file_path = 'cars.json'


with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    cars_list = [row for row in csv_reader]


with open(json_file_path, mode='w') as json_file:
    json.dump(cars_list, json_file, indent=2)

# завернуть все в функцию
=======
import csv
import json


csv_file_path = 'cars.csv'
json_file_path = 'cars.json'


with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    cars_list = [row for row in csv_reader]


with open(json_file_path, mode='w') as json_file:
    json.dump(cars_list, json_file, indent=2)

# завернуть все в функцию
