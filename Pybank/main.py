import csv

# Define the file path
file_path = 'budget_data.csv'

# Initialize variables
total_months = 0
net_total = 0
previous_profit_losses = None
changes = []
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}

# Open and read the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Update the total number of months
        total_months += 1

        # Update the net total amount of "Profit/Losses"
        current_profit_losses = int(row['Profit/Losses'])
        net_total += current_profit_losses

        # Calculate changes in "Profit/Losses"
        if previous_profit_losses is not None:
            change = current_profit_losses - previous_profit_losses
            changes.append(change)

            # Check for the greatest increase in profits
            if change > greatest_increase['amount']:
                greatest_increase = {'date': row['Date'], 'amount': change}

            # Check for the greatest decrease in profits
            if change < greatest_decrease['amount']:
                greatest_decrease = {'date': row['Date'], 'amount': change}

        # Set the previous_profit_losses for the next iteration
        previous_profit_losses = current_profit_losses

# Calculate the average change in "Profit/Losses"
average_change = sum(changes) / len(changes)

# Print the analysis results
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
