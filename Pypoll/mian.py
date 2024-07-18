import csv

# Load the dataset
file_path = 'election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Count total votes
        total_votes += 1
        
        # Count votes per candidate
        candidate = row['Candidate']
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate percentage of votes each candidate won and find the winner
result_lines = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    result_lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Create the formatted result string
result = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
result += "\n".join(result_lines)
result += "\n-------------------------\n"
result += f"Winner: {winner}\n"
result += "-------------------------\n"

# Display the result
print(result)
