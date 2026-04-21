# Week 3 – Competency Claim (C2 & C3)

In this assignment, I improved a buggy Python script that processes messy CSV survey data so that it runs without errors and produces clean output.

The original script crashed with the error:
ValueError: invalid literal for int() with base 10: 'fifteen'

I identified that this was caused by non-numeric values in the "experience_years" column. To fix this, I introduced a helper function `parse_experience()` that uses a try/except block to safely handle invalid values and skip them during calculation. This change is documented in my commit:
"fix: handle non-numeric experience_years values like 'fifteen' using try/except"

I also corrected a sorting issue where the script was not returning the highest satisfaction scores. I updated the sorting logic to ensure the top 5 results are ordered correctly in descending order.

To improve readability and maintainability, I added inline comments explaining key steps such as loading data, cleaning values, and processing results. The script now also writes cleaned data to a new file, `week3_survey_cleaned.csv`, ensuring consistent and reusable output.

This work demonstrates my ability to read error messages, diagnose data issues, modify code, and document changes clearly.