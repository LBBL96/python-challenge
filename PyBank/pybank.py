import csv

# Setting up lists to drop our dates and profits into
dates = []
profit = []

# Setting months variable, which we'll be counting in our data
months = 0

pybank_csv = "budget_data.csv"

with open(pybank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)

# Deleting the header so we don't count it or include it in lists
    next(csvreader)

# As we read in each row, we're creating lists of dates and profits, and counting months
    
    for row in csvreader:
        dates.append(row[0])
        profit.append(row[1])
        months = months + 1
        

# # Removing first values from our lists, since they're not relevant
# dates.remove("Date")
# profit.remove("Profit/Losses")

# Converting the strings in the profit list to integers. Variable name slightly changed.
profits = [int(x) for x in profit]

# Summing the integers in the profit list gives us the net total
net_total = sum(profits)



# Output

print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {months}")
print(f"Total: ${net_total}")
