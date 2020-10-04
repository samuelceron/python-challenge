import os
import csv

budget_data_path = os.path.join('Resources','budget_data.csv')

total_months = 0
total_budget = 0
average_change = 0
max_change = 0
min_change = 0
previous = 0
current_value = 0
total_changes = 0

with open(budget_data_path,  "r", newline="") as budget_data:
    csv_reader  = csv.reader(budget_data, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_changes += 1
        total_months += 1
        total_budget += int(row[1])

        current_value = row[1]
        change = int(current_value) - int(previous)
        previous = current_value
        print(change)

        if (change > max_change):
            max_change = change
            max_date_change = row[0]
        
        if (change < min_change):
            min_change = change
            min_date_change = row[0]
    

print (total_months)
print (total_budget)
print (max_change)
print (min_change)
print (total_changes)
print (max_date_change)
print (min_date_change)

print(
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_budget}\n"
   f"Average  Change: 0\n"
   f"Greatest Increase in Profits: {max_date_change} {max_change}\n"
   f"Greatest Decrease in Profits: {min_date_change} {min_change}\n"
    )