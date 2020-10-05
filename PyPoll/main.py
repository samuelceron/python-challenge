import os
import csv

election_data_path = os.path.join('Resources','election_data.csv')

#Set variables and intialiazing 
total_votes = 0

with open(election_data_path, "r", newline="") as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1

print(total_votes)