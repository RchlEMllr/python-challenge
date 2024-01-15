#importing the functions I will need: OS for opening and creating files, CSV to read CSV files, and statistics for the average
import os
import csv
import statistics

#opening the source .csv file 
csvpath = os.path.join("python-challenge/PyBank/Resources/budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #to skip header when counting 
    next(csvreader)
    #declaring variables I will need later 
    month_count = 0
    change = []
    total_change = 0
    avg_change = 0
    max_change = 0
    min_change = 0
    max_month = ''
    min_month = ''

    for row in csvreader:
        month_count = month_count + 1
        total_change = total_change + int(row[1])
        change.append(int(row[1]))
        #I cannot for the life of me make the number match yours in the example results 
        #here is how I calculated the average change
        avg_change = statistics.median(change)
        #finds the largest number in the column
        #actually I don't see the number from the example in the source file at all so maybe that's why I can't make the average work
        max_change = max(change)
        #finds the smallest number in the column
        min_change = min(change)
        #compares the min and max against the months and matches them to print to results
        changes = float(row[1])
        if changes==max_change: 
            max_month = row[0]      
        if changes==min_change:
            min_month = row[0]

    #printing results to terminal    
    print("Financial Analysis")
    print("----------------------------")
    print (f"Total Months: {month_count}")
    print (f"Total: ${total_change}")
    print (f"Average Change: ${avg_change}")
    print (f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

#opening .txt results file
output_file = os.path.join("python-challenge/PyBank/analysis/financial_analysis.txt")
#writing results to .txt file, including \n for paragraphs
with open(output_file, 'w') as txt:
    txt.write("Financial Analysis\n")
    txt.write("----------------------------\n")
    txt.write(f"Total Months: {month_count}\n")
    txt.write(f"Total: ${total_change}\n")
    txt.write(f"Average Change: ${avg_change}\n")
    txt.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
    txt.write(f"Greatest Decrease in Profits: {min_month} (${min_change})")

