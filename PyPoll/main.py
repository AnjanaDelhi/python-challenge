# Import the os module for creating file paths and the csv module for reading csv files
import os
import csv

# Get the Relative path (get by right clicking on the file)- PyBank\Resources\budget_data.csv. Then load the file path as a variable. 
file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

#Creating variables needed
total_votes = 0
candidates = []
votes_candidate = []
percent = []
max_votes = 0

  
# Read the file using csv module and storing the contents as "csvfile"
with open(file_path) as csvfile:
    election_data = csv.reader(csvfile, delimiter= ',') #csv.reader function needs the variable and delimiter.
    # Do not include the header row 
    next(election_data, None)
    #print(f"CSV Header: {file_1_header}")

    
    # Loop for total months 
    for row in election_data:
        #naming rows to make it easier
        voter_id = str(row[0])
        county = str(row[1])
        nominee = str(row[2])

        #Total votes
        total_votes += 1 

        # finding unique candidates votes and adding the unique candidates to the candidate list
        if nominee in candidates:
            nominee_index = candidates.index(nominee)
            votes_candidate[nominee_index] += 1

        else:
            candidates.append(nominee)
            votes_candidate.append(1)

    # Calculation of percent of votes for each candidate and appending to a list percent, we need a loop for this
    for i in range(len(candidates)):
        percent_each = round(((votes_candidate[i]/total_votes)*100), 4)
        percent.append(percent_each)

    # Figure out the Winner by either max percent or max votes   
        if votes_candidate[i] > max_votes:
            max_votes = votes_candidate[i]
            max_index = i

    winner = candidates[max_index]
        
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------")

# we dont know the total number of candidates hence we write a loop for the length of candidates
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent[i]}% ({votes_candidate[i]})")

print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

# Writing a text output file
# In python text files, each line of text is terminated with a special character called EOL (End of Line), which is the new line character (‘\n’) in python by default.

# Creating a file path
output_path = os.path.join("PyPoll", "Analysis", "output.txt")

with open(output_path, "w") as output_file:
    
    # Writing the first row
    output_file.write("Election Results \n")
    # Rest of the rows
    output_file.write("------------------------------------- \n")

    output_file.write(f"Total Votes: {total_votes} \n")

    output_file.write("------------------------------------- \n")
   
    for i in range(len(candidates)):
        output_file.write(f"{candidates[i]}: {percent[i]}% ({votes_candidate[i]}) \n")

    output_file.write("------------------------------------- \n")
    output_file.write(f"Winner: {winner} \n")   
    output_file.write("------------------------------------- \n")