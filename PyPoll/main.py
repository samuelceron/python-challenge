import os
import csv

#election_data_path = os.path.join('Resources','test.csv')
election_data_path = os.path.join('Resources','election_data.csv')

#Set variables and intialiazing 
total_votes = 0
candidates_list=[]
votes_list=[]
percent_list=[]
candidate_total=[]

with open(election_data_path, "r", newline="") as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1

        #Getting the candidates list
        if row[2] not in candidates_list:
            candidates_list.append(row[2])

        votes_list.append(row[2])
   
    for candidate in candidates_list:
        candidate_total.append(votes_list.count(candidate))
        percent_list.append(((votes_list.count(candidate))/(total_votes))*100)

winner = candidates_list[candidate_total.index(max(candidate_total))]
print(candidates_list)
print(candidate_total)
#print(votes_list)
print(percent_list)

print(
   f"Election Results\n"
   f"----------------------------\n"
   f"Total Votes: {total_votes}\n"
   f"----------------------------\n")
for i in range(len(candidates_list)):
        print(f'{candidates_list[i]}: {(percent_list[i]):3.3f}% ({candidate_total[i]})')
print(
    f"----------------------------\n"
   f"Winner: {winner}\n"
    )
#Set exit path
analysis_file_path = os.path.join('Analysis','analysis.txt')
with open(analysis_file_path,"w") as analysis_file:
    analysis_file.write(f"Election Results\n")
    analysis_file.write(f"----------------------------\n")
    analysis_file.write(f"Total Votes: {total_votes}\n")
    for i in range(len(candidates_list)):
        analysis_file.write(f'{candidates_list[i]}: {(percent_list[i]):3.3f}% ({candidate_total[i]})\n')
    analysis_file.write(f"----------------------------\n")
    analysis_file.write( f"Winner: {winner}\n")
