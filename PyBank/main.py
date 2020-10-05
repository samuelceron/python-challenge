import os
import csv

budget_data_path = os.path.join('Resources','budget_data.csv')

#Set variables and intialiazing 
total_months = 0
total_budget = 0
average_change = 0
max_change = 0
min_change = 0
previous = 0
current_value = 0
total_changes = -1
total_in_changes = 0

#Get the first row after header to set it to 'previous'
with open(budget_data_path,  "r", newline="") as budget_data:
    csv_reader  = csv.reader(budget_data, delimiter=",")
    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    previous = first_row[1]

#Iterate only without header
with open(budget_data_path,  "r", newline="") as budget_data:
    csv_reader  = csv.reader(budget_data, delimiter=",")
    csv_header = next(csv_reader)

#Loop through rows of CSV
    for row in csv_reader:

        #Calculate total changes, months and profits/losses
        total_changes += 1
        total_months += 1
        total_budget += int(row[1])

        #Calculate changes
        current_value = row[1]
        change = int(current_value) - int(previous)
        previous = current_value
        #print(change)

        #Calculate greatest decrease and increase
        if (change > max_change):
            max_change = change
            max_date_change = row[0]
        
        if (change < min_change):
            min_change = change
            min_date_change = row[0]
        
        #Calculate total in changes for the average
        total_in_changes = (total_in_changes) + change 
average_change = round((float((total_in_changes)/total_changes)),2)

#Demo console prints
# print (total_months)
# print (total_budget)
# print (max_change)
# print (min_change)
# print (total_changes)
# print (max_date_change)
# print (min_date_change)
# print(average_change)

#Generate output and TXT fyle with results
output=(
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_budget}\n"
   f"Average  Change: {average_change}\n"
   f"Greatest Increase in Profits: {max_date_change} (${max_change})\n"
   f"Greatest Decrease in Profits: {min_date_change} (${min_change})\n"
    )
analysis_file_path = os.path.join('Analysis','analysis.txt')
with open(analysis_file_path,"w") as analysis_file:
    analysis_file.write(output)