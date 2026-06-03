# MP2 Competency Claim(s)

This MP2 demonstrates my ability to build a complete computational tool for an HCD research workflow. In `mini-project-2/mp2_notebook.ipynb`, I built a notebook that takes a survey CSV as input and turns open-ended responses into a first-pass theme summary with reusable outputs.

The strongest evidence is the working pipeline in the notebook. I used pandas to rename messy survey columns, extract short-answer fields, reshape the data into a long response table, remove blank responses, assign keyword-based themes, and count theme frequency. The main analysis operations include `melt()`, filtering, `explode()`, `value_counts()`, and `groupby()`.

The tool also produces concrete outputs that another researcher can review: `mini-project-2/output/theme_frequency.csv`, `mini-project-2/output/example_responses_by_theme.csv`, `mini-project-2/output/theme_summary_report.md`, and `mini-project-2/charts/theme_frequency.png`. These files show that the notebook is not only exploratory analysis, but a small repeatable tool that generates tables, examples, a chart, and a report.

A key judgment in the project is that unmatched responses are labeled as `Other / unclear` instead of being forced into a theme. This keeps the limits of the keyword-based method visible and makes the output more appropriate as a first-pass synthesis aid rather than a final qualitative coding result.