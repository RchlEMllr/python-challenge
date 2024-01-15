#importing the functions I will need: OS for opening and creating files, CSV to read CSV files
import os
import csv

#opening the source .csv file 
csvpath = os.path.join("python-challenge/PyPoll/Resources/election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #declaring variables
    total_votes = 0
    cand1 = "1"
    cand2 = "2"
    cand3 = "3" 
    cand1_votes = 0
    cand2_votes = 0
    cand3_votes = 0
    cand1_per = 0
    cand2_per = 0
    cand3_per = 0
    win_votes = 0
    winner = "?"

    #to skip header when counting 
    next(csvreader)
    for row in csvreader:

        #counter for total votes
        total_votes = total_votes + 1

        #grabbing first candidate name
        if cand1 == '1': 
            cand1 = row[2]
        #grabbing second candidate name
        if row[2] != cand1 and cand2 == '2': 
            cand2 = row[2]
        #grabbing third candidate name
        elif row[2] != cand1 and row[2] != cand2:
            cand3 = row[2]

        #counter for candidates 1 and 2 and anything else is candidate 3
        if row[2] == cand1: cand1_votes = cand1_votes + 1
        elif row[2] == cand2: cand2_votes = cand2_votes + 1
        else: cand3_votes = cand3_votes + 1

#calculating percentage with number of votes per canddidate divided by total votes
cand1_per = round(float((cand1_votes/total_votes)*100),3)
cand2_per = round(float((cand2_votes/total_votes)*100),3)
cand3_per = round(float((cand3_votes/total_votes)*100),3)

#determining the highest number of candidate votes
win_votes = max(cand1_votes, cand2_votes, cand3_votes)
#assigning winner to the candidate with the matching number
if win_votes == cand1_votes: winner = cand1
elif win_votes == cand2_votes: winner = cand2
else: winner = cand3

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{cand1}: {cand1_votes} ({cand1_per}%)")
print(f"{cand2}: {cand2_votes} ({cand2_per}%)") 
print(f"{cand3}: {cand3_votes} ({cand3_per}%)")
print("-------------------------")
print(f"Winner: {winner}")


#opening .txt results file
output_file = os.path.join("python-challenge/PyPoll/analysis/election_results.txt")
#writing results to .txt file, including \n for paragraphs
with open(output_file, 'w') as txt:
    txt.write("Election Results\n")
    txt.write("-------------------------\n")
    txt.write(f"Total Votes: {total_votes}\n")
    txt.write("-------------------------\n")    
    txt.write(f"{cand1}: {cand1_votes} ({cand1_per}%)")
    txt.write(f"{cand2}: {cand2_votes} ({cand2_per}%)") 
    txt.write(f"{cand3}: {cand3_votes} ({cand3_per}%)")
    txt.write("-------------------------")
    txt.write(f"Winner: {winner}")
