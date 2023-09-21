#Import the os module: allow us to create paths across operating systems & Module for reading csv files
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

totalprofit=0
totalmonth=0
prevprofit=0
change=0
totalchange=0
monthlychange=0
greatestprofit=0
greatestprofitmonth=""
greatestdecrease=0
greatestdecmonth=""



#You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)

    for row in csvreader:
        totalmonth = totalmonth + 1
        totalprofit = totalprofit + int(row[1])

        currentprofit = int(row[1])
        
        if prevprofit != 0:
            
            change= currentprofit-prevprofit
            totalchange= totalchange + change
            monthlychange= monthlychange + 1

        prevprofit = currentprofit

        if change > greatestprofit:
            greatestprofit=change
            greatestprofitmonth = row[0]

        if change < greatestdecrease:
            greatestdecrease = change
            greatestdecmonth = row[0]








#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#• The total number of months included in the dataset
#• The net total amount of "Profit/Losses" over the entire period
#• The changes in "Profit/Losses" over the entire period, and then the average of those changes
#• The greatest increase in profits (date and amount) over the entire period
#• The greatest decrease in profits (date and amount) over the entire period


output=f"""
Financial Analysis
----------------------------
Total Months: {totalmonth}
Total: ${totalprofit}
Average Change: ${totalchange / monthlychange:.2f}
Greatest Increase in Profits: {greatestprofitmonth} (${greatestprofit})
Greatest Decrease in Profits: {greatestdecmonth} (${greatestdecrease})
"""



print(output)

with open("analysis/budget.txt", 'w') as outfile:
    outfile.write(output)