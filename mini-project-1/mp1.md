# MP1 Competency Claim

For Mini Project 1, I created a published Jupyter notebook that analyzes a sample of the Seattle Police Department Crime Data 2008–Present dataset. The notebook uses `data/seattle_crime_sample.csv` and is organized as a complete analysis story: overview, data profile, analysis, conclusions, and process.

In the data profile section, I used pandas to inspect the dataset with `df.head()`, `df.info()`, `df.describe()`, and `df.isnull().sum()`. This helped me understand the shape of the data, the column types, and which missing values might matter for the analysis.

I prepared the data by converting offense date fields into datetime values and creating new time-based columns, including `Hour`, `Month`, `Year`, `Day of Week`, and `Time Period`. I then used pandas operations such as `value_counts()`, `dropna()`, filtering, and `groupby()` to answer my analysis questions about when reported offenses happen, where they are reported, and how offense sub-categories differ across parts of the day.

The notebook includes three Plotly charts. The first chart shows reported crime counts by hour of day. The second chart uses a horizontal bar chart to show the top 10 Seattle neighborhoods by reported offenses. The third chart uses a grouped bar chart to compare common offense sub-categories across morning, afternoon, evening, and night. Each chart has a clear title, labeled axes, a markdown interpretation, and a saved PNG file in the `charts/` folder.

I also made careful interpretation choices rather than over-claiming from the data. For example, the neighborhood chart shows where more offenses were reported, but I do not claim that those neighborhoods are automatically more dangerous. Higher report counts could also reflect population density, commercial activity, nightlife, policing patterns, or reporting behavior.