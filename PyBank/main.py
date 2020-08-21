# Import the os module for creating file paths and the csv module for reading csv files
import os
import csv

# Get the Relative path (get by right clicking on the file)- PyBank\Resources\budget_data.csv. Then load the file path as a variable. 
file_path = os.path.join("PyBank", "Resources", "budget_data.csv")

#Creating variables needed
total_months = 0
net_total = 0
last_profit = 0
profit_change = []
average_change = []
increase = ['', 0]
decrease = ['', 999999999999999999]

# Read the file using csv module and storing the contents as "csvfile"
with open(file_path) as csvfile:
    file_original = csv.reader(csvfile, delimiter= ',') #csv.reader function needs the variable and delimiter.
    # Do not include the header row 
    next(file_original, None)
    #print(f"CSV Header: {file_1_header}")

    # Loop for total months 
    for row in file_original:
        total_months += 1 
        net_total = net_total + int(row[1])
        #Getting the profit chage each month
        profit_change = int(row[1]) - last_profit
        #Resetting the last_profit to the next month
        last_profit = int(row[1])
        #Adding the values to the profit_change list to calculate the average 
        #profit_change.append(double(row[1]))
        # Calculating the average
        average_change = round((net_total/total_months), 2)
        # or average_change = sum(profit_change)/len(profit_change)
        
        if (profit_change > increase[1]):
            # Greatest increase value
            increase[1] = profit_change
            # Greatest increase month
            increase[0] = row[0]

        if (profit_change < decrease[1]):
            # Greatest increase value
            decrease[1] = profit_change
            # Greatest increase month
            decrease[0] = row[0]
        
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average change: ${average_change}")
print(f"Greatest Increase in Profits: {increase[0]} (${increase[1]})")
print(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})")

# Writing a text output file
# In python text files, each line of text is terminated with a special character called EOL (End of Line), which is the new line character (‘\n’) in python by default.

# Creating a file path
output_path = os.path.join("PyBank", "Analysis", "output.txt")

with open(output_path, "w") as output_file:
    
    # Writing the first row
    output_file.write("Financial Analysis \n")
    # Rest of the rows
    output_file.write("------------------------------------- \n")

    output_file.write(f"Total Months: {total_months} \n")
   
    output_file.write(f"Total: ${net_total} \n")
    
    output_file.write(f"Average change: ${average_change} \n")
   
    output_file.write(f"Greatest Increase in Profits: {increase[0]} (${increase[1]}) \n") 
    
    output_file.write(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]}) \n")

       