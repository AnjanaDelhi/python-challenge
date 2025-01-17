# Import the os module for creating file paths and the csv module for reading csv files
import os
import csv

# Get the Relative path (get by right clicking on the file)- PyBank\Resources\budget_data.csv. Then load the file path as a variable. 
file_path = os.path.join("PyBank", "Resources", "budget_data.csv")

#Creating variables needed
total_months = 0
net_total = 0
last_profit = 0
total_profit_change = []
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

        #naming rows to make it easier
        date = str(row[0])
        profit = int(row[1])
        
        #total months
        total_months += 1 
        #Net total
        net_total = net_total + profit

        #Getting the profit chage each month
        profit_change = profit - last_profit

        #Resetting the last_profit to the current month
        last_profit = profit
        

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
        

#Adding the values to the profit_change list to calculate the average 
        if profit_change != profit:
            total_profit_change.append(profit_change)

    #print(total_profit_change)
    #print(len(total_profit_change))

# Calculating the average
#average_change = round((net_total/total_months), 2)
average_change = round((sum(total_profit_change)/len(total_profit_change)), 2)
        
                
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

       