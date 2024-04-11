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
total_months = []
profit_losses = []
changes = []
# open the file
with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    next(csv_file)
    #read row in the file
    for row in csv_file:
        # add to total months
        total_months.append(row[0])
        # total amount of profit/losses
        profit_losses.append(int(row[1]))
    # changes in profit/losses
    for i in range(len(profit_losses)-1):
        changes.append(profit_losses[i+1]-profit_losses[i])

    





# print the results to screen
# print('Financial Analysis')
# print('----------------------------')
#print(f'Total Months: {len(total_months)}')
#print(f'Total: ${sum(profit_losses)}')
print(f'Average Change: {round(sum(changes)/len(changes),2)}')
### end here

# example output
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
