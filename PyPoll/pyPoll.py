# PyPoll

import os
import csv

# Path to collect data from the Resources folder
pyElect_csv = os.path.join('election_data.csv')
Khan = 0
Correy = 0
Li = 0
OTooley = 0
others = 0
total_votes = 0


# Reading the csv file

with open(pyElect_csv, "r") as csvfile:
    votes = csv.reader(csvfile, delimiter = ',')
    header = next(votes)
    
    # reading row by row

#     for row in votes:
#         total_votes = total_votes + 1
#         if row[] == "Marsh":
#             marsh = marsh + 1
#     print(marsh)
#     print(total_votes)
        
    for row in votes:
        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == Li:
            Li = Li + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "O'Tooley":
            OTooley = OTooley + 1
        else:
            others = others + 1
        total_votes = total_votes + 1
#     print(f"Khan got {Khan} votes, Correy got {Correy} votes, Li got {Li} votes, O'Tooley got {OTooley} votes.")
#     print(f"Other votes: {others}")
#     print(f"Total votes were: {total_votes}")
    Khan_p = round((Khan/total_votes),5) * 100
    Correy_p = round((Correy/total_votes),5) * 100
    Li_p = round((others/total_votes),5) * 100
    OTooley_p = round((OTooley/total_votes),5) * 100
    winner = max(Khan, Correy, Li, OTooley, others)
    

    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    print(f"Khan : {Khan_p}% ({Khan})")
    print(f"Correy : {Correy_p}% ({Correy})")
    print(f"Li : {Li_p}% ({others})")
    print(f"O'Tooley : {OTooley_p}% ({OTooley})")
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")