# Import the CSV
import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#Create empty lists for the data
date = []
budget = []
changes = []

# Open and Read the CSV File
with open(budget_data, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    header = next(reader)

# Append the csv data to the empy lists
    for row in reader:
        date.append(row[0])
        budget.append(int(row[1]))

# Calculate the total number of months included in the dataset
total_months = len(date)
# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = sum(budget)
# Calculate the changes in "Profit/Losses" over the entire period, and the average
for i in range(1, len(budget)):
    change = budget[i] - budget[i-1]
    changes.append(change)
average_change = sum(changes) / len(changes)

# What is the greatest increase in profits (date and amount) over the entire period?
max_index = budget.index(max(budget))
increase_date = date[max_index]
increase_amount = max(budget)
# What is the greatest decrease in profits (date and amount) over the entire period?
min_index = budget.index(min(budget))
min_date = date[min_index]
min_amount = min(budget)

print(f"""
Financial Analysis
Total Months: {total_months}
Total: ${net_total}
Average Change: {average_change:.2f}
Greatest Increase in Profits: {increase_date} ({increase_amount})
Greatest Decrease in Profits: {min_date} ({min_amount})
"""
)


