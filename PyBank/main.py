import os
import csv

budget_data_path = os.path.join('Resources','budget_data.csv')

with open(budget_data_path,  "r", newline="") as budget_data:
    csv_reader  = csv.reader(budget_data, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        print(row)