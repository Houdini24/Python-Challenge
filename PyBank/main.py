# Import the CSV
import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

# Create lists to store the data
month = []
day = []
profit = []

# Open and Read the CSV File
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Split the month from the day
    for row in csv_reader:
        # Split the month from the day
        split_column = row[0].split("-")
        month.append(split_column[0])
        day.append(split_column[1])
        profit.append(row[1])




# Calculate the total number of months included in the dataset
#total_months = 
# Calculate the net total amount of "Profit/Losses" over the entire period
#total =

# Calculate the changes in "Profit/Losses" over the entire period, and the average
#average_change = 

# What is the greatest increase in profits (date and amount) over the entire period?
#highest_increase = 
# What is the greatest decrease in profits (date and amount) over the entire period?
#highest_decrease = 

#Print the title
#print('Financial Analysis')
#Print the total months in the dataset
#print('Total Months:' + total_months)
#Print the net total profit/losses
#print('Total:' + total)
#Print the total changes
#print('Average Change:' + average_change)
#Print the greatest profits
#print('Greatest Increase in Profits:' + highest_increase)
#Print the greatest losses
#print('Greatest Decrease in Profits:' + highest_decrease)


