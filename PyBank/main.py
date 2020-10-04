import os
import csv

budget_data_path = os.path.join('Resources','budget_data.csv')

total_months = 0
total_budget = 0
average_change = 0
max_change = 0
min_change = 0

with open(budget_data_path,  "r", newline="") as budget_data:
    csv_reader  = csv.reader(budget_data, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        print(row)
        total_months += 1
        total_budget += int(row[1])

print (total_months)
print (total_budget)

print(
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_budget}\n"
   f"Average  Change: 0\n"
   f"Greatest Increase in Profits: \n"
   f"Greatest Decrease in Profits: \n"
    )