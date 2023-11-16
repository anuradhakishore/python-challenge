import os
import csv


month = 0                                                               #Initialising total months
total_amount = 0                                                        #Initialising total profit and loss
total_change = 0                                                        #Initialising total change in profit and loss
previous_amount = 0                                                     #Initialising previous line amout for change calculation
max_change = 0                                                          #Initialising greatest increase in profit
min_change = 0                                                          #Initialising greatest decrease in profit
max_date = ""                                                           #Initialising date for greatest increase in profit
min_date = ""                                                           #Initialising date for greatest decrease in profit

os.chdir(os.path.dirname(__file__))                                     # Change directory to the directory of current python script


csvpath = os.path.join("Resources", "budget_data.csv")                  # Path to collect data from the Resources folder


with open(csvpath, 'r') as csvfile:                                     #Reading the CSV files
    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)                                        #Storing header row

    for line in csvreader:                                              #Iterating through CSV files
        month += 1                                                      #calculating the total month count
        total_amount += int(line[1])                                    #calculating the total amount for profit and loss

        if month > 1:                                                   #Calculating the changes in profits, over adjacent months
            change = int(line[1]) - previous_amount
            total_change += change                                      #adding the total changes month over month

            if change > max_change:                                     #calculating greatest increase in profit
                max_change = change
                max_date = line[0]

            if change < min_change:                                     #calculating greatest decrese in profit
                min_change = change
                min_date = line[0]

        previous_amount = int(line[1])                                  #Previous amount assignment for next calculations, each time

average = round(total_change / (month - 1),2)                                    #Average change

#prinitng the results

print("Financial Analysis")

print("-----------------------------------------------------------------")

print("Total Months:", month)
print(f"Total: ${total_amount}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {max_date} (${max_change})" )
print(f"Greatest Decrease in Profits: {min_date} (${min_change})")

#Output the financial results to tex file named financialanalysis.txt

budget_file = os.path.join("Analysis", "financialanalysis.txt")
with open(budget_file, "w") as file:


 file.write("Financial Analysis" + "\n")

 file.write("-----------------------------------------------------------" + "\n")

 file.write(f"Total Months: {month}\n")

 file.write(f"Total: ${total_amount}\n")

 file.write(f"Average change: ${average}\n")

 file.write(f"Greatest Increase in Profits: {max_date} (${max_change})" + "\n")

 file.write(f"Greatest Decrease in Profits: {min_date} (${min_change})" + "\n")
      
 file.close()