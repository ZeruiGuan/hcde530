import csv

# Helper function to safely convert experience values to integers
def parse_experience(value):
    """Convert experience to int; return None if invalid."""
    value = value.strip()
    try:
        return int(value)
    except ValueError:
        return None

# Load the survey data from a CSV file
filename = "week3_survey_messy.csv"
rows = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    # Read each row from the input CSV file and store it in a list
    for row in reader:
        rows.append(row)

role_counts = {}

for row in rows:
    # Normalize role names so variations like "ux researcher" are counted the same
    role = row["role"].strip().title()
    if role in role_counts:
        role_counts[role] += 1
    else:
        role_counts[role] = 1

print("Responses by role:")
for role, count in sorted(role_counts.items()):
    print(f"  {role}: {count}")

# Calculate the average years of experience
total_experience = 0
valid_experience_count = 0
cleaned_rows = []

# Use helper function to skip invalid experience values like "fifteen"
for row in rows:
    experience = parse_experience(row["experience_years"])

    if experience is not None:
        total_experience += experience
        valid_experience_count += 1
        row["experience_years"] = str(experience)
    else:
        row["experience_years"] = ""

    cleaned_rows.append(row)

avg_experience = total_experience / valid_experience_count
print(f"\nAverage years of experience: {avg_experience:.1f}")

# Find the top 5 highest satisfaction scores
scored_rows = []
# Collect rows that have a valid satisfaction score
for row in rows:
    if row["satisfaction_score"].strip():
        scored_rows.append((row["participant_name"], int(row["satisfaction_score"])))

# Sort scores from highest to lowest to get the top 5 results
scored_rows.sort(key=lambda x: x[1], reverse=True)
top5 = scored_rows[:5]

print("\nTop 5 satisfaction scores:")
for name, score in top5:
    print(f"  {name}: {score}")

# Write the cleaned survey data to a new CSV file
with open("week3_survey_cleaned.csv", "w", newline="", encoding="utf-8") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)
