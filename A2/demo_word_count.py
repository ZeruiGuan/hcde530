import csv


# Load the CSV file
filename = "demo_responses.csv"
responses = []

# Open the CSV file so the script can read all survey responses
with open(filename, newline="", encoding="utf-8") as f:
    # Read the CSV file and treat each row as a dictionary using column names as keys
    reader = csv.DictReader(f)
    # Save each row so we can process all responses later
    for row in reader:
        responses.append(row)


# Define a helper function to count the number of words in a response
def count_words(response):
    """Count the number of words in a response string.

    Takes a string, splits it on whitespace, and returns the word count.
    Used to measure response length across all participants.
    """
    return len(response.split())


# Count words in each response and print a row-by-row summary
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)

word_counts = []

for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]

    # Count how many words are in this participant's response
    count = count_words(response)
    word_counts.append(count)

    # Shorten long responses so they fit nicely in the output table
    if len(response) > 60:
        preview = response[:60] + "..."
    else:
        preview = response

    print(f"{participant:<6} {role:<22} {count:<6} {preview}")

print()
# Print summary statistics for all responses
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
print(f"  Shortest        : {min(word_counts)} words")
print(f"  Longest         : {max(word_counts)} words")
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
