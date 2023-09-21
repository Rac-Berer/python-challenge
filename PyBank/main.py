
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