# handling paths
import os

# module for reading CSV files
import csv

# path to CSV file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")


    first_data_line = next(csvreader) # read first data entry
    compare_entry = int(first_data_line[1]) # set first price
    total = compare_entry # add price to total
    months = 1 # this is the first month
    sum_of_differences = 0 # no difference for first month
    greatest_increase_difference = 0 # ^
    greatest_decrease_difference = 0 # ^^
    
    for row in csvreader: # statement iterates over the rows in the CSV file
        months += 1 # add months
        current_entry = int(row[1]) # get current margin
        difference = current_entry - compare_entry # compute margin difference
        total += current_entry # add to total
        sum_of_differences += difference # compute sum of differences
        average_change = round(sum_of_differences/(months-1), 2)
        if difference >= greatest_increase_difference: # compare current difference to largest seen value
            greatest_increase_difference = difference # if true, change to new difference value
            greatest_increase_month = str(row[0]) # store the month this happened
        elif difference <= greatest_decrease_difference: # reverse of above
            greatest_decrease_difference = difference
            greatest_decrease_month = str(row[0])
            
        # reset for next loop
        compare_entry = current_entry # the current value is pushed to the 'old' value
        #print(row[0], difference) # will print month and difference from previous month for each row
            
# The total number of months included in the dataset
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_difference})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_difference})")
list_of_lines = ["Financial Analysis", "----------------------------", "Total Months: " + str(months), "Total: " + '$' + str(total), "Average Change: " + '$' + str(average_change), "Greatest Increase in Profits: " + str(greatest_increase_month) + ' ' + '$' + str(greatest_increase_difference), "Greatest Decrease in Profits: " + str(greatest_decrease_month) + ' ' + '$' + str(greatest_decrease_difference)]

    
# Set variable for output file
output_file = os.path.join(".", "analysis", "budget_data_final.txt")
    
#  Open the output file
with open(output_file, "w") as datafile:
    for line in list_of_lines: 
        datafile.write(''.join(line) + '\n')
