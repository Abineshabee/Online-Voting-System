import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("ovs.db")

# Create a cursor object
cursor = conn.cursor()

# Execute a query to select all rows from the 'vote' table
cursor.execute("SELECT * FROM vote")

# Fetch all the rows
data = cursor.fetchall()

# Close the connection
conn.close()

# Initialize a dictionary to store votes for each candidate
candidate_votes = {}

# Iterate through the fetched data and calculate votes for each candidate
for row in data:
    candidate = row[1]  # Candidate name is in the second column (index 1)
    votes = int(row[2]) # Convert vote count to an integer
    
    # Update the candidate's vote count in the dictionary
    candidate_votes[candidate] = candidate_votes.get(candidate, 0) + votes

# Save the data to a file
with open("Data.txt", "w") as file:
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {votes} votes\n")

