# Survey Theme Summarizer for Student Transportation Research

## What the Tool Does

This is a Jupyter notebook tool that takes a CSV of open-ended survey responses and turns them into a first-pass theme summary. It extracts short-answer responses, assigns keyword-based themes, counts theme frequency, and generates output files.

## Who It Is For

This tool is for student UX researchers who need a quick way to summarize open-ended survey feedback before writing research findings.

## Public URL

Published Jupyter notebook on GitHub:

https://github.com/ZeruiGuan/hcde530/blob/main/mini-project-2/mp2_notebook.ipynb

## How to Run It

You can view the notebook directly on GitHub using the public URL above.

To run it locally:

1. Open `mini-project-2/mp2_notebook.ipynb` in Jupyter Notebook, JupyterLab, or Cursor.
2. Make sure the input CSV is located at `mini-project-2/data/student_transportation_survey.csv`.
3. Run the notebook from top to bottom.

The notebook generates:

- `output/theme_frequency.csv`
- `output/example_responses_by_theme.csv`
- `output/theme_summary_report.md`
- `charts/theme_frequency.png`