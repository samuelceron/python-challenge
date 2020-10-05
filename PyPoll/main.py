import os
import csv

election_data_path = os.path.join('Resources','election_data.csv')

#Set variables and intialiazing 
total_votes = 0
candidates_list=[]

with open(election_data_path, "r", newline="") as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")
    csv_header = next(csv_reader)

    #Getting the candidates list
    for row in csv_reader:
        total_votes += 1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])

print(candidates_list)

print(
   f"Election Results\n"
   f"----------------------------\n"
   f"Total Votes: {total_votes}\n"
   f"----------------------------\n"
   f"Votes: \n"
   f"----------------------------\n"
   f"Winner: \n"
    )
