# Import the CSV
import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

#Open and Read the CSV File
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Calculate the total number of votes cast

#List all candidates who received votes

#Find the percentage of votes each candidate won

#Find the total number of votes each candidate won

#Find the winner of the election based on popular vote