import os
import csv

csvpath = os.path.join('PyPoll','Resources','election_data.csv')

votes=0
candidate=0
totalvotes=0
winningvotes = 0
winner=""
candidate_outputlist = []


candidates_dict={}
candidate_list = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)
    
    for row in csvreader:
        totalvotes = totalvotes + 1
        votes = (row[0])
        candidate = (row[2])


        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidates_dict[candidate] = 0

        candidates_dict[candidate] = candidates_dict[candidate] + 1

    for candidate in candidates_dict:
        votes = candidates_dict[candidate]
        percentvotes = round(votes / totalvotes * 100,3)

        candidate_outputlist.append(f'{candidate}: {percentvotes}% ({votes})')
        if votes > winningvotes:
            winningvotes=votes
            winner = candidate


output=f"""
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
{candidate_outputlist[0]}
{candidate_outputlist[1]}
{candidate_outputlist[2]}
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open("PyPoll/analysis/budget.txt", 'w') as outfile:
    outfile.write(output)