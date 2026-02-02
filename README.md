# Kaggle Student Data Analysis Project

## Description
This project is based on a Kaggle-style dataset created and analyzed using Python.
The data is treated like a small student database.

Using pandas and if-else logic, student performance is analyzed based on marks,
attendance, and department.

## What This Project Does
- Creates student data using Python
- Converts data into a pandas DataFrame
- Filters students by department
- Calculates average marks
- Applies if-else logic to assign Pass/Fail status
- Sorts and filters data based on conditions

## Concepts Used
- Python dictionaries
- Pandas DataFrame
- If-else conditions
- Lambda functions
- Data filtering and sorting

## Key Code Logic (Sample)

```python
import pandas as pd

# Create student dataset
students = {
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Department": ["CS", "IT", "CS", "IT"],
    "Marks": [78, 45, 88, 62]
}

# Convert to DataFrame
df = pd.DataFrame(students)

# Calculate average marks
average_marks = df["Marks"].mean()

# Assign Pass/Fail using conditional logic
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Filter CS students and sort by marks
cs_students = df[df["Department"] == "CS"].sort_values(by="Marks", ascending=False)



## What I Learned
- How to work with real-world style data
- How to apply conditional logic on datasets
- How to analyze data using pandas
- How to upload Kaggle projects to GitHub

## File
- kaggletask.ipynb → Main Kaggle data analysis notebook
