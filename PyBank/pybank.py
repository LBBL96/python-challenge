import csv

# I couldn't figure out how to build a dataframe, so I decided to approach this problem using lists.
# I've created two to hold the two columns of our data: dates and profit.
dates = []
profit = []

# Setting months variable, which we'll be counting as the data is read into the script.
months = 0

# Path to the csv and then the command to read it as a csv.

pybank_csv = "budget_data.csv"

with open(pybank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)

# Skipping the header so we don't count it for months or include it in lists
    next(csvreader)

# As we read in each row, we're appending the dates and profits, and counting months (which conveniently
# equals the number of rows we have)
    
    for row in csvreader:
        dates.append(row[0])
        profit.append(row[1])
        months = months + 1
        

# Since the list interpreted the profit as strings, I'll need to convert the numbers to integers. 
# I've changed the variable name to prevent any problems with overwriting the original list.
profits = [int(x) for x in profit]

# Summing the integers in the profit list gives the net total
net_total = sum(profits)

# I want to create a new list that shifts the values of the list of profits
# one place to the left so that I can subtract each month's profit from the previous month. I'm removing
# the first value and then appending a zero to the end so that the lists will be the same length.

profits_shifted_left = []
profits_shifted_left = profits[1:]
profits_shifted_left.append(0)

# I want to make a list comprehension to subtract the elements of one list from their corresponding
# elements in the second list. To make things less messy-looking, I'm assigning the lists to 
# variables x and y. This new list, profit_diff, contains the differences between the profits of a month
# and the profit of the previous month.

x = profits_shifted_left
y = profits
profit_diff = [x - y for x, y in zip(x,y)]

# To get an index that tells me what month the profit change occurs in, I'll create a dictionary where the
# keys are the months and the values are the profit differences. First I'll need to shift the dates once
# to the left so that they will connect the difference with the ending month. I'll do this by slicing.

date_key = []
date_key = dates[1:]

# To keep the date_key list the same length as the dates list, I'll append zero to the end.
date_key.append(0)

# Now I can create a dictionary of dates corresponding to the profit changes.

keys = date_key
values = profit_diff
my_dict = dict(zip(keys, values))

# Now I need to find the greatest increase and greatest decrease in profits.

max_inc = max(profit_diff)
max_dec = min(profit_diff)

# To see what month the max and min occur in, I need to locate the key that corresponds to it.

max_key = [key for (key, value) in my_dict.items() if value == max_inc]
min_key = [key for (key, value) in my_dict.items() if value == max_dec]

# To make it pretty for the output, I'll need to recast the keys as strings and slice the [''] off.

greatest = str(max_key)
greatest = greatest[2:-2]
least = str(min_key)
least = least[2:-2]

# To compute the average profit/loss, I'll need to create another list that slices off the last
# number in my profit_diff list, since it's not part of my difference.

profit_diff2 = profit_diff[:-1]

# Now I'll compute the average profit/loss. Since we have one less difference in the list than we
# have months, I'll divide by months - 1. I'll also use the round function.

average = round(sum(profit_diff2)/(months-1), 2)

# Now I'll output the financial analysis.

printout = (

    "\nFinancial Analysis\n"
    "----------------------------\n"
    f"Total Months : {months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {greatest}  (${max_inc})\n"
    f"Greatest Decrease in Profits: {least}  (${max_dec})\n"

)

print(printout)

# Finally, I'll output the file to txt.

output_path = "pybank.txt"
with open(output_path, 'w') as txt:
    txt.write(printout)