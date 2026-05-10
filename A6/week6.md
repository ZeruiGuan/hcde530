# Week 6 — C6 Data Visualization Claim

For A6, I created three Plotly charts from the Seattle Police Department Crime Data 2008–Present dataset. The goal was not just to make charts, but to use each chart to answer one part of my MP1 analysis: when reported offenses happen, where they are concentrated, and how offense types differ across time periods.

## Chart 1: Reported Crime Counts by Hour of Day

I used a vertical bar chart because I am comparing reported offense counts across ordered hour categories from 0 to 23. This chart type fits the data because each hour is a separate category, and the bar heights make the differences easy to compare.

The chart shows that reported offenses are not evenly distributed across the day. Hour 0 has the highest count, early morning hours around 3–6 AM are lower, and counts rise again from late morning through evening. One thing to be careful about is that this chart shows recorded offense counts by hour, not exact crime risk by hour.

## Chart 2: Top 10 Seattle Neighborhoods by Reported Offenses

I used a horizontal bar chart because the chart compares neighborhood categories, and some neighborhood names are long. A horizontal layout makes the labels easier to read than a vertical chart.

The chart shows that reported offenses are concentrated in a smaller set of neighborhoods. Downtown Commercial has the highest count, followed by Capitol Hill and Northgate. I filtered out the `-` value because it does not represent an actual neighborhood. This chart should not be read as a direct ranking of “most dangerous” neighborhoods because it uses raw counts and does not adjust for population, neighborhood size, visitors, or reporting differences.

## Chart 3: Most Common Offense Sub-Categories by Time Period

I used a grouped bar chart because I am comparing multiple offense sub-categories across morning, afternoon, evening, and night. This chart type fits the question because it lets me compare both the time periods and the offense sub-categories in one view.

I used `Offense Sub Category` instead of the broader `Offense Category` field because `Offense Category` only has three broad groups. The sub-category field gives a more specific view of the kinds of offenses in the dataset. I also removed vague values like `ALL OTHER` and `999` so the chart focuses on more meaningful offense types.

The chart shows that Larceny-Theft is the largest sub-category across all four time periods. Night has the highest count for several common sub-categories. This chart shows counts only, not rates adjusted by population, activity level, or exposure.

## C6 Competency Claim

I demonstrated C6 by choosing chart types that fit the data structure and the analytical question. I used a bar chart for hourly count comparison, a horizontal bar chart for neighborhood categories with long labels, and a grouped bar chart for comparing offense sub-categories across time periods.

My Jupyter notebook includes the code, saved chart outputs, and markdown explanations so another reader can follow how I loaded the dataset, prepared the fields, created the charts, and interpreted the findings. Together, the charts make specific findings visible: temporal patterns, spatial concentration, and offense-type differences in Seattle crime reports.