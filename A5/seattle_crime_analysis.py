import pandas as pd

# A5 Pandas Analysis: Seattle Crime Data
# Dataset: Seattle Police Department Crime Data 2008–Present
# File name: SPD_Crime_Data__2008-Present_20260501.csv

# Analytical questions:
# 1. How do reported crime counts vary by hour of day, day of week, and month in Seattle?
# 2. Which Seattle precincts, sectors, or neighborhoods have the highest number of reported offenses?
# 3. How do the most common offense categories differ across time periods, such as morning,
#    afternoon, evening, and night?

# Why this matters:
# I am interested in how public safety data can reveal patterns in urban life.
# Looking at time, location, and offense category can help make a large public dataset
# easier to understand and connect to human-centered planning and decision-making.


# 1. Load the dataset

# This loads the Seattle crime CSV into pandas so I can work with it as a table.
# Once the data is in a DataFrame, I can inspect its structure and summarize patterns.
# The CSV file should be stored in the same folder as this Python script.
df = pd.read_csv(
    "SPD_Crime_Data__2008-Present_20260501.csv",
    low_memory=False
)


# 2. Data Profile

# I first check the dataset size because I want to know the scale of the analysis.
# The result tells me how many offense records and columns are included.
print("\n--- Dataset Shape ---")
print(df.shape)


# Looking at the first few rows helps me understand what a single record looks like.
# This also gives me a quick check that the file loaded correctly.
print("\n--- First Five Rows ---")
print(df.head())


# This gives a more detailed overview of the columns, data types, and non-null counts.
# I use this to confirm that the dataset has the time, offense, and location fields needed for my questions.
print("\n--- Dataset Info ---")
df.info()


# I print the column names so I can use the exact field names in the rest of the script.
# This helps prevent mistakes caused by guessing or using column names from a different version of the dataset.
print("\n--- Column Names ---")
print(df.columns)


# This missing-value check shows whether any columns have blank values recognized by pandas.
# It helps me decide which fields may need extra caution before drawing conclusions.
print("\n--- Missing Values by Column ---")
print(df.isnull().sum())


# This gives a first summary of the main offense categories.
# It shows which broad types of offenses make up most of the dataset.
print("\n--- Top 10 Offense Categories ---")
print(df["Offense Category"].value_counts().head(10))


# 3. Prepare time columns

# The offense date is stored as text, so I convert it into a datetime value.
# This step makes it possible to analyze crime records by hour, weekday, month, and year.
# I specify the format because the dates in this CSV look like "2016 Mar 15 02:21:00 PM".
df["Offense Date"] = pd.to_datetime(
    df["Offense Date"],
    format="%Y %b %d %I:%M:%S %p",
    errors="coerce"
)


# These new columns break the full date into smaller time units.
# They let me compare reported offenses across hours, weekdays, months, and years.
df["Hour"] = df["Offense Date"].dt.hour
df["Day of Week"] = df["Offense Date"].dt.day_name()
df["Month"] = df["Offense Date"].dt.month_name()
df["Year"] = df["Offense Date"].dt.year


# I preview the new time columns to make sure the transformation worked.
# If these values look correct, I can use them for the time-based analysis.
print("\n--- Time Columns Preview ---")
print(df[["Offense Date", "Hour", "Day of Week", "Month", "Year"]].head())


# Question 1:
# How do reported crime counts vary by hour of day, day of week, and month in Seattle?

# This count shows how reported offenses are distributed across the 24 hours of the day.
# It helps identify whether reports cluster around certain times.
print("\n--- Reported Offenses by Hour of Day ---")
hour_counts = df["Hour"].value_counts().sort_index()
print(hour_counts)


# This count compares reported offenses across weekdays.
# It helps show whether some days have more reported activity than others.
print("\n--- Reported Offenses by Day of Week ---")
weekday_counts = df["Day of Week"].value_counts()
print(weekday_counts)


# This count summarizes reported offenses by month.
# It gives an initial view of whether reporting volume changes across the year.
print("\n--- Reported Offenses by Month ---")
month_counts = df["Month"].value_counts()
print(month_counts)


# I also check year counts because this dataset covers a long time range.
# This helps me see whether the records are evenly distributed over time or concentrated in certain years.
print("\n--- Reported Offenses by Year ---")
year_counts = df["Year"].value_counts().sort_index()
print(year_counts)


# Question 2:
# Which Seattle precincts, sectors, or neighborhoods have the highest number of reported offenses?

# This summarizes reported offenses by precinct, which is a broad geographic category.
# It shows where reports are most concentrated at the police precinct level.
print("\n--- Reported Offenses by Precinct ---")
precinct_counts = df["Precinct"].value_counts(dropna=False)
print(precinct_counts)


# Sector is more detailed than precinct, so this gives a more specific location breakdown.
# The top sectors help identify smaller areas with high numbers of offense records.
print("\n--- Top 15 Sectors by Reported Offenses ---")
sector_counts = df["Sector"].value_counts(dropna=False).head(15)
print(sector_counts)


# This looks at neighborhood labels to see which named areas appear most often.
# I need to interpret this carefully because many records use "-" instead of a real neighborhood name.
print("\n--- Top 15 Neighborhoods by Reported Offenses ---")
neighborhood_counts = df["Neighborhood"].value_counts(dropna=False).head(15)
print(neighborhood_counts)


# This is a groupby version of the precinct count.
# It confirms the precinct-level pattern by counting offense IDs within each precinct.
print("\n--- Grouped Offense Count by Precinct ---")
precinct_grouped = df.groupby("Precinct")["Offense ID"].count().sort_values(ascending=False)
print(precinct_grouped)


# This combines location and offense type in one summary.
# It helps show which offense categories are most common within the highest-volume neighborhood labels.
print("\n--- Top Neighborhood and Offense Category Combinations ---")
neighborhood_offense_counts = (
    df.groupby(["Neighborhood", "Offense Category"])
    .size()
    .sort_values(ascending=False)
    .head(20)
)
print(neighborhood_offense_counts)


# Question 3:
# How do the most common offense categories differ across time periods?

# This function turns each hour into a broader part of the day.
# Grouping records this way makes it easier to compare morning, afternoon, evening, and night.
def assign_time_period(hour):
    if pd.isnull(hour):
        return "Unknown"
    elif 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"


# I apply the time period labels to every row.
# The new column gives me a simpler way to compare offense patterns across the day.
df["Time Period"] = df["Hour"].apply(assign_time_period)


# This checks how many records fall into each time period.
# It shows whether one part of the day has noticeably more reported offenses than the others.
print("\n--- Records by Time Period ---")
print(df["Time Period"].value_counts())


# This summary compares offense categories within each time period.
# It helps show whether the most common offense types change depending on the time of day.
print("\n--- Top 20 Time Period and Offense Category Combinations ---")
time_offense_counts = (
    df.groupby(["Time Period", "Offense Category"])
    .size()
    .sort_values(ascending=False)
    .head(20)
)
print(time_offense_counts)


# This table puts time periods and offense categories side by side.
# It is easier to compare category counts across the day in this format.
print("\n--- Offense Category Counts by Time Period ---")
time_offense_table = (
    df.groupby(["Time Period", "Offense Category"])
    .size()
    .unstack(fill_value=0)
)
print(time_offense_table)


# Here I focus only on nighttime records.
# This subset lets me see which broad offense categories are most common at night.
night_crimes = df[df["Time Period"] == "Night"]

print("\n--- Top 10 Offense Categories at Night ---")
print(night_crimes["Offense Category"].value_counts().head(10))


# I also create a morning subset for comparison.
# Comparing morning and night helps show whether category patterns shift across the day.
morning_crimes = df[df["Time Period"] == "Morning"]

print("\n--- Top 10 Offense Categories in the Morning ---")
print(morning_crimes["Offense Category"].value_counts().head(10))


# 4. Additional critical data check: reports vs. offenses

# I compare unique report numbers with unique offense IDs because they are not the same thing.
# This tells me whether my analysis is counting offense records or unique police reports.
unique_reports = df["Report Number"].nunique()
unique_offenses = df["Offense ID"].nunique()

print("\n--- Unique Reports and Unique Offenses ---")
print("Unique Report Numbers:", unique_reports)
print("Unique Offense IDs:", unique_offenses)


# This shows whether some report numbers appear many times.
# If they do, it means one police report can contain multiple offenses, which affects how raw counts should be interpreted.
print("\n--- Report Numbers That Appear Most Often ---")
print(df["Report Number"].value_counts().head(10))


# These outputs give me an initial answer to my three questions about time, location,
# and offense category patterns in the Seattle crime dataset.