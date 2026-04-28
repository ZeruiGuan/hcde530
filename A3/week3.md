# Week 3 – Competency Claim

While debugging the script, I encountered a `ValueError: invalid literal for int() with base 10: 'fifteen'` when the code attempted to convert the `experience_years` field using `int()`. This showed that the dataset contained non-numeric values, which violated the assumption that all entries in that column were numeric and caused the script to crash at runtime.

To fix this, I implemented a helper function with a try/except block to safely parse values and skip invalid entries. This made the script robust to messy, real-world data instead of failing on unexpected input.

I also fixed a logic bug where satisfaction scores were sorted in ascending order, which incorrectly returned the lowest 5 scores instead of the highest. This revealed that a script can run without errors but still produce incorrect analysis results if the logic is wrong.

Fixing these two bugs showed that working with messy data requires both handling invalid values and verifying analysis logic. This matters because incorrect parsing or sorting would lead to misleading averages or rankings, which would affect any decisions based on this data.
