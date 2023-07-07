# handling paths
import os

# module for reading CSV files
import csv

# path to csv
csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    candidate_name_and_vote_tally = {} # dictionary will map candidate names to the number of votes they have received
    total_votes = 0 # initializing total number of votes
    
    for row in csvreader: # statement iterates over the rows in the CSV file        
        candidate_name = str(row[2]) # statement gets the candidate's name from the row
        total_votes += 1 # add votes
        if candidate_name in candidate_name_and_vote_tally: # statement checks if the candidate's name is in the dictionary. If the candidate's name is in the dictionary, the code will increment the vote count for that candidate
            candidate_name_and_vote_tally[candidate_name] += 1 # add candidate's vote
        else: # statement executes if the candidate's name is not in the dictionary. In this case, the code will add the candidate's name to the dictionary and set the vote count to 1
            candidate_name_and_vote_tally[candidate_name] = 1 # starts new candidate tally


    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    list_of_lines = ["Election Results", "----------------------------", "Total Votes: " + str(total_votes), "----------------------------"]

    winning_vote_count = 0 # initializing winning candidate
    winning_candidate = None # sets blank
    
    for candidate_name, vote_count in candidate_name_and_vote_tally.items(): # statement iterates over the items in the dictionary
        percentage_of_votes = round((vote_count / total_votes)*100, 3) # rounds vote percentage to three decimal places
        if vote_count >= winning_vote_count: # compare current vote count to largest seen value
            winning_vote_count = vote_count # if true, change to new vote count value
            winning_candidate = candidate_name # states winning candidate
        print(f"{candidate_name}: {percentage_of_votes}% ({vote_count})")
        list_of_lines.append([str(candidate_name) + ': ' + str(percentage_of_votes) + '% (' + str(vote_count) + ')'])
        
    print("----------------------------")
    print(f"Winner: {winning_candidate}")
    print("----------------------------")
    list_of_lines.append(["----------------------------", "Winner: " + str(winning_candidate), "----------------------------"])
    
    # Set variable for output file
    output_file = os.path.join(".", "analysis", "election_data_final.txt")
    
    #  Open the output file
    with open(output_file, "w") as datafile:
        for line in list_of_lines: 
            datafile.write(''.join(line) + '\n')
