import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

votes=0
candidate=0
totalvotes=0
winner=""
candidate1=""
candidate1votes=0
candidate1percent=0.000
candidate2percent=0.000
candidate2=""
candidate2votes=0
candidate3percent=0.000 
candidate3=""
candidate3votes=0

dict=({"candidate1":"Charles Casper Stockham","candidate2":"Diana DeGette", "candidate3":"Raymon Anthony Doane"})

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)
    
    for row in csvreader:
        totalvotes = totalvotes + 1
        votes = (row[0])
        candidate = (row[2])

        if candidate == "candidate1":
            candidate1 = candidate1
            candidate1votes = candidate1votes + 1
            candidate1percent = candidate1votes/totalvotes * 100

        if candidate == "candidate2":
            candidate2votes = candidate2votes + 1
            candidate2percent = candidate2votes/totalvotes * 100

        if candidate == "candidate3":
            candidate3votes = candidate3votes + 1
            candidate3percent = candidate3votes/totalvotes * 100

        if candidate1votes > candidate2votes and candidate1votes > candidate3votes:
            candidate1 = winner

            winner = candidate1

        if candidate2votes > candidate1votes and candidate2votes > candidate3votes:
            candidate2 = winner

            winner = candidate2

        if candidate3votes > candidate1votes and candidate3votes > candidate2votes:
            candidate3 = winner

            winner = candidate3


        dict["Charles Casper Stockham"]= candidate1
        dict["Diana DeGette"]= candidate2
        dict["Raymon Anthony Doane"]= candidate3


output=f"""
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
{candidate1}: {candidate1percent}% ({candidate1votes})
{candidate2}: {candidate2percent}% ({candidate2votes})
{candidate3}: {candidate3percent}% ({candidate3votes})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open("analysis/budget.txt", 'w') as outfile:
    outfile.write(output)