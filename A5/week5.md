# Week 5 Competency Claim

In `seattle_crime_analysis.py`, I used pandas to analyze the Seattle Police Department Crime Data 2008–Present CSV for my Mini Project 1. The script loads the dataset from a CSV file and works with fields such as `Offense Date`, `Offense Category`, `Precinct`, `Sector`, `Neighborhood`, `Report Number`, and `Offense ID`.

I used `head()` and `info()` to inspect the structure of the dataset, which showed that the file contains 1,531,135 offense records and 20 columns. I used `isnull().sum()` to check for missing values, and `value_counts()` to summarize common offense categories, time patterns, precincts, sectors, and neighborhoods. I also used filtering to compare morning and nighttime records, and `groupby()` to summarize counts by precinct and by time period plus offense category.

The analysis gave initial answers to my three questions: when reported offenses happen, where they are concentrated, and how offense categories differ across time periods. For example, North and West precincts had the highest reported offense counts, and nighttime had the highest count among my time-period groups. I also noticed that many `Neighborhood` values are recorded as `-`, so neighborhood-level findings need caution.

One important data decision was to count offense records instead of assuming every row is a unique police report. I checked this by comparing `Report Number` and `Offense ID`, which showed fewer unique report numbers than unique offense IDs. This matters because some reports include multiple offenses, so my outputs should be described as offense counts.

The CSV file is not included in GitHub because it is larger than GitHub's file size limit. The dataset is available from Seattle Open Data: https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5/about_data