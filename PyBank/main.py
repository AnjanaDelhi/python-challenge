# Import the os module for creating file paths and the csv module for reading csv files
import os
import csv

# Get the Relative path (get by right clicking on the file)- PyBank\Resources\budget_data.csv. Then load the file path as a variable. 
file_path = os.path.join("PyBank", "Resources", "budget_data.csv")

#Creating variables needed
total_months = 0
net_total = 0
average_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]

# Read the file using csv module and storing the contents as "csvfile"
with open(file_path) as csvfile:
    file_1 = csv.reader(csvfile, delimiter= ',') #csv.reader function needs the variable and delimiter.
    print(file_1)
    # Read the header row first 
    file_1_header = next(file_1)
    print(f"CSV Header: {file_1_header}")

    # Loop for total months 
    for row in file_1:
        total_months = total_months + 1 
        net_total = net_total + int(row[1])
        average_change = net_total/ len(row[1])

        
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {net_total}")
    print(f"Average change: {average_change}")
       