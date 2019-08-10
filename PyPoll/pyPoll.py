# # PyPoll

import csv

pyElect_csv = 'election_data.csv'

# I'm creating two lists: one to collect the names of candidates, and one to collect their vote count
candidates = []
cand_count = []
counter = 0
#count = 0


with open(pyElect_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)

# Skipping the header so we don't count it for months or include it in lists
    next(csvreader)

# As we read in each row, we're appending the dates and profits, and counting months (which conveniently
# equals the number of rows we have)
    
    for row in csvreader:
        
        if row[2] not in candidates:
            candidates.append(row[2])
            cand_count.append(0)
        cand_num = len(candidates)
        #count = count + 1
        
    
        for counter in range(0, cand_num):
            
            if row[2] == candidates[counter]:
                cand_count[counter] = cand_count[counter] + 1
                
                
        
    
    
        
#     for row in csvreader:
#         print(row[2])
#         for counter in range(0,cand_num-1):
#             print(row[2])
#             if row[2] == candidates[counter]:
#                 cand_count[counter] = cand_count[counter] + 1
#                 print(row[2])
        
            
        
names = candidates
votes = cand_count
print(names)
print(votes)
# print(count)

# import csv

# # Path to collect data from the Resources folder
# pyElect_csv = os.path.join('election_data.csv')
# Khan = 0
# Correy = 0
# Li = 0
# OTooley = 0
# others = 0
# total_votes = 0


# # Reading the csv file

# with open(pyElect_csv, "r") as csvfile:
#     votes = csv.reader(csvfile, delimiter = ',')
#     header = next(votes)
    
#     # reading row by row

# #     for row in votes:
# #         total_votes = total_votes + 1
# #         if row[] == "Marsh":
# #             marsh = marsh + 1
# #     print(marsh)
# #     print(total_votes)
        
#     for row in votes:
#         if row[2] == "Khan":
#             Khan = Khan + 1
#         elif row[2] == Li:
#             Li = Li + 1
#         elif row[2] == "Correy":
#             Correy = Correy + 1
#         elif row[2] == "O'Tooley":
#             OTooley = OTooley + 1
#         else:
#             others = others + 1
#         total_votes = total_votes + 1
# #     print(f"Khan got {Khan} votes, Correy got {Correy} votes, Li got {Li} votes, O'Tooley got {OTooley} votes.")
# #     print(f"Other votes: {others}")
# #     print(f"Total votes were: {total_votes}")
#     Khan_p = round((Khan/total_votes),5) * 100
#     Correy_p = round((Correy/total_votes),5) * 100
#     Li_p = round((others/total_votes),5) * 100
#     OTooley_p = round((OTooley/total_votes),5) * 100
#     winner = max(Khan, Correy, Li, OTooley, others)
    

#     print("Election Results")
#     print("--------------------------")
#     print(f"Total Votes: {total_votes}")
#     print("--------------------------")
#     print(f"Khan : {Khan_p}% ({Khan})")
#     print(f"Correy : {Correy_p}% ({Correy})")
#     print(f"Li : {Li_p}% ({others})")
#     print(f"O'Tooley : {OTooley_p}% ({OTooley})")
#     print("--------------------------")
#     print(f"Winner: {winner}")
#     print("--------------------------")