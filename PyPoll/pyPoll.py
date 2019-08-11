# PyPoll

# Something clicked for me when I was doing the banking exercise: I realized that I was getting
# mentally blocked trying to figure out how to drop lists into datasets. I've done a lot of mathematical
# study over the past two years, and the answer suddenly popped out at me: these aren't just lists we're 
# working with -- they're arrays. When I started thinking about them mathematically, I realized that 
# operations could be performed on the elements of one list/array using the elements of another. 

# As usual, I'm starting by importing the csv library.
import csv

# Path
pyElect_csv = 'election_data.csv'

# I'm creating two lists: one to collect the names of candidates, and one to collect their vote count.
candidates = []
vote_count = []

# This counter won't be used in the standard incremental way, but rather to form the indices of an array.
# counter = 0

# Starting the with block to read in the file.
with open(pyElect_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)

# Skipping the header so that it won't be included in the lists.
    next(csvreader)

# I'm starting to scan the dataset row by row.
    for row in csvreader:

        # row[2] is the row index that contains the candidate name. I'm looking at the rows one by one
        # to see if the candidate's name has appeared yet. If it hasn't, I'm appending it to my candidate list.
        # This method will let me run any dataset where the third column is candidate names -- no matter how 
        # many different candidates are in the dataset.
        if row[2] not in candidates:
            candidates.append(row[2])
            
            # This is not an intuitive piece of code, and was the fruit of a lot of experimentation. What this
            # does is create a placeholder for the new candidate in the vote_count array/list. The next
            # for loop will populate this placeholder.
            vote_count.append(0)

            # The last line of this if loop tells us the length of the candidate name array/list. This is important 
            # because the next for loop is going to use this length to determine the end point of the range
            # function. This is the number of different candidates.
        num_of_candidates = len(candidates)
        
        # The range function is really useful here. I set the end of the range to the number of candidates.
        # Here's what's really cool about it: the range is dynamic. There's no need to count a candidate's votes
        # until that candidate's name appears. When a new name appears, the length of the candidates list 
        # increments by one, and thus, so does the length of the range we're cycling through.
        for counter in range(0, num_of_candidates):
            
            # Here's where that placeholder in vote_count that I set up in the first for loop gets filled.
            # Each candidate has his/her own index (in this dataset, 0-3) and the counter will fill the
            # vote_count list/array with the number of votes that corresponds to the index number in the
            # candidates list/array.
            if row[2] == candidates[counter]:
                vote_count[counter] = vote_count[counter] + 1
                
# That's it! Starting at "for row in csvreader:" there are only 8 lines of code! Can you tell I'm proud? ;)
    
# Now that I've read all of election_data.csv, my two lists/arrays are filled. To make the list names
# shorter for the later print statements, I'm renaming them.     
names = candidates
votes = vote_count

# I realized that I don't need to make a dictionary to connect keys to values because the array indices
# match up. It was harder to see this in the banking code, so I didn't make that logical leap.
# A print statement (which I'm leaving out, but definitely looked at along the way) shows that the two
# lists look like this: 
# names = ['Khan', 'Correy', 'Li', "O'Tooley"]
# votes = [2218231, 704200, 492940, 105630]

# I'll define some variables to make printing simpler.
total_votes = sum(votes)

# First we need to determine the max number in the votes list.
most_votes = max(votes)

# The index function will return the index for the place in the list where most_votes occurs. For simplicity,
# I'm assigning it to the variable i.
i = votes.index(most_votes)

# To find the winner, all I need to do is call the most_votes index within the names list.
winner = names[i]

# To get the percentage of votes each candidate received, I'll divide each element in the list "votes"
# by total_votes, multiply each fraction by 100, and round to two places. I'll drop each of these 
# percentages into a new list. 
percent = []
for vote in votes:
    unrounded = (vote/total_votes)*100
    per = round(unrounded, 2)
    percent.append(per)

# To make it easy to output to text, I'll create a variable called printout and populate it with
# my total_votes and winner variables and with the three lists called by index. Ideally, it would contain a 
# dynamic list of candidates, but I wasn't able to figure out how to do that in time.

printout = (
    "\nElection Results\n"
    "--------------------------\n"
    f"Total Votes: {total_votes}\n"
    "--------------------------\n"
    f"{names[0]} : {percent[0]}% ({votes[0]})\n"
    f"{names[1]} : {percent[1]}% ({votes[1]})\n"
    f"{names[2]} : {percent[2]}% ({votes[2]})\n"
    f"{names[3]} : {percent[3]}% ({votes[3]})\n"
    "--------------------------\n"
    f"Winner: {winner}\n"
    "--------------------------"
    )

# I could print a dynamic list of candidates and their corresponding percentages and votes, but I don't
# know that I can place it within a variable. Without being able to do that, I can't put it in the printout
# variable above. If I were simply outputting to the screen, I'd run the block of code below between
# print statements for Election Results and Winner.

#  for i in range(0,len(candidates):
#      print(f"{names[i]} : {percent[i]}% ({votes[i]})")


# Output to screen
print(printout)

# Finally, I'll output the file as a text file
output_path = "pypoll.txt"
with open(output_path, 'w') as txt:
    txt.write(printout)

# I'm really proud of this code. It took a lot of work and a lot of experimentation to get it right.