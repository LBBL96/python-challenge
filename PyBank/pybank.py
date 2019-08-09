import os
import csv

net_profit = 0

# Path to collect data from the Resources folder
pybank_csv = os.path.join('BudgetData.csv')

# Reading the csv file

with open(pybank_csv, "r") as csvfile:
    budget_data = csv.reader(csvfile, delimiter = ',')
    header = next(budget_data)

    for row in budget_data:
        net_profit = row[1] + net_profit
    print(net_profit)

