# Import the CSV
import os
import csv

#Create the path to the CSV file
election_data = os.path.join("Resources", "election_data.csv")

# Create an empty list for the number of ballots
ballot_id = []
#Create a dictionary for the different candidates
candidates = {}
# Start the count of votes at 0 so they can be added
total_votes = 0

#Open and Read the CSV File
with open(election_data, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    header = next(reader)

#Create a for loop to calculate 
    # the total number of votes cast
    # all candidates who received votes
    # the total number of votes each candidate won
    for row in reader:
        ballot_id.append(row[0])
        candidate = row[2]
        total_votes += 1

# Create an if/else statement to find 
    # the percentage of votes each candidate won
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print "Election Results"
    print("Total Votes:", total_votes)
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(candidate + ": {:.2f}% ({})".format(percentage, votes))
# Find the winner of the election based on popular vote
    winner = max(candidates, key=candidates.get)
    print("Winner:", winner)
