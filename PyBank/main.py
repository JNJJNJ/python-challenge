import csv
# 
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in profits (date and amount) over the entire period

### start here
#create variables
budget_file_path = r"PyBank\Resources\budget_data.csv"
# open the file
with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    #read row in the file
    for row in csv_file:
        #total number of months
        months = []
        profit_losses = []
        changes = []

        for row in csv_file:
            months.append(row[0])

profit_losses.append(int(row[1]))

# calculate the total number of months
total_months = len(months)


# calculate the changes in profit/losses and store them in a list

### end here

# example output
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# print('Financial Analysis')
# print('----------------------------')
# print('Total Months:')
# print('Total:')
# print('Average Change:')
# print('Greatest Increase in Profits:')
# print('Greatest Decrease in Profits:')