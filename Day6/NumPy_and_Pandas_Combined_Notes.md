
------------------------------------------------------------------------

# Part 2: Pandas -- DataFrames, Filtering, Missing Values and Data Cleaning

## 1. What is Pandas?

Pandas is a Python library used for data manipulation and analysis.

It helps: - Load CSV, Excel, and JSON datasets. - Organize data into
rows and columns. - Filter records using conditions. - Detect and handle
missing values. - Remove duplicate records. - Prepare datasets for
analysis and machine learning.

Install and import:

``` bash
pip install pandas numpy
```

``` python
import pandas as pd
import numpy as np
```

## 2. Understanding a DataFrame

A DataFrame is a two-dimensional tabular data structure containing rows
and columns, similar to an Excel spreadsheet.

``` python
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Age": [21, 22, 20, 23, np.nan],
    "Marks": [85, 90, np.nan, 78, 88],
    "City": ["Delhi", "Jaipur", "Delhi", "Mumbai", "Jaipur"]
}

df = pd.DataFrame(data)
print(df)
```

`NaN` represents a missing value.

## 3. Loading a Dataset

Load a CSV file:

``` python
df = pd.read_csv("students.csv")
print(df)
```

Other formats:

``` python
df = pd.read_excel("students.xlsx")
df = pd.read_json("students.json")
```

Save a DataFrame as CSV:

``` python
df.to_csv("cleaned_students.csv", index=False)
```

`index=False` prevents Pandas from writing the DataFrame index as an
additional column.

## 4. Inspecting a Dataset

Inspect the dataset before cleaning or analyzing it.

  Function / Attribute   Purpose
  ---------------------- -----------------------------------------------------
  `df.head()`            Displays the first 5 rows
  `df.head(10)`          Displays the first 10 rows
  `df.tail()`            Displays the last 5 rows
  `df.shape`             Returns number of rows and columns
  `df.info()`            Shows column names, data types, and non-null counts
  `df.describe()`        Gives descriptive statistics for numeric columns
  `df.columns`           Displays column names
  `df.dtypes`            Displays data types of columns

Example:

``` python
print(df.head())
print("Shape:", df.shape)
df.info()
print(df.describe())
print("Columns:", df.columns)
print("Data types:\n", df.dtypes)
```

For example, `(1000, 5)` means 1,000 rows and 5 columns.

## 5. Handling Missing Values

Missing values occur when information is not available for a particular
record.

### 5.1 Detect missing values

``` python
print(df.isnull())
print(df.isnull().sum())
```

-   `isnull()` returns `True` where a value is missing.
-   `isnull().sum()` counts missing values in each column.

Percentage of missing values:

``` python
print(df.isnull().mean() * 100)
```

### 5.2 Remove missing values with `dropna()`

``` python
# Remove rows containing at least one missing value
df_without_missing_rows = df.dropna()

# Remove rows where every value is missing
df_without_empty_rows = df.dropna(how="all")

# Remove columns containing missing values
df_without_missing_columns = df.dropna(axis=1)

# Remove rows with missing values in selected columns
df_without_missing_age = df.dropna(subset=["Age"])
```

`dropna()` returns a cleaned DataFrame by default; it does not modify
the original DataFrame unless assigned back or used with an appropriate
in-place option.

### 5.3 Fill missing values with `fillna()`

Instead of deleting records, missing values can be replaced.

**Mean:** Average of numerical values. Often useful when the
distribution has no strong outliers.

``` python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

**Median:** Middle value after sorting. Often useful when numerical data
contains outliers.

``` python
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
```

**Mode:** Most frequently occurring value. Useful for categorical
columns.

``` python
df["City"] = df["City"].fillna(df["City"].mode()[0])
```

  -----------------------------------------------------------------------
  Method                  Meaning                 Common use
  ----------------------- ----------------------- -----------------------
  `dropna()`              Removes missing records When removing them is
                          or columns              justified

  `fillna(mean)`          Replaces missing values Numerical data without
                          with the mean           strong outliers

  `fillna(median)`        Replaces missing values Numerical data with
                          with the median         outliers

  `fillna(mode)`          Replaces missing values Categorical data
                          with the most frequent  
                          value                   
  -----------------------------------------------------------------------

**Important:** Choose a missing-value strategy based on the meaning and
distribution of the data. For machine-learning workflows, calculate
imputation values from the training data only, then apply them to
validation and test data to avoid data leakage.

## 6. Filtering DataFrame Rows

Filtering selects records that satisfy one or more conditions.

Example DataFrame:

``` python
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Age": [21, 22, 20, 23, 24],
    "Marks": [85, 90, 75, 78, 88],
    "City": ["Delhi", "Jaipur", "Delhi", "Mumbai", "Jaipur"]
}

df = pd.DataFrame(data)
```

### 6.1 Filter using one condition

Students scoring more than 80:

``` python
result = df[df["Marks"] > 80]
print(result)
```

### 6.2 Filter using multiple conditions (AND)

Students scoring above 80 and older than 21:

``` python
result = df[(df["Marks"] > 80) & (df["Age"] > 21)]
print(result)
```

### 6.3 Filter using OR

Students from Delhi or Jaipur:

``` python
result = df[(df["City"] == "Delhi") | (df["City"] == "Jaipur")]
print(result)
```

### 6.4 Filter using `isin()`

``` python
result = df[df["City"].isin(["Delhi", "Mumbai"])]
print(result)
```

### 6.5 Select specific columns using `loc[]`

Display only the name and marks of students scoring above 80:

``` python
result = df.loc[df["Marks"] > 80, ["Name", "Marks"]]
print(result)
```

Logical operators:

  Operator   Meaning
  ---------- ---------
  `&`        AND
  `|`        OR
  `~`        NOT

Use parentheses around each condition when combining conditions.

## 7. Practical Task: Load, Inspect, Clean, and Filter a Dataset

This example creates a small student dataset, inspects it, handles
missing values, filters students, and saves the cleaned data.

### Step 1: Create a sample dataset

``` python
import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit", "Karan"],
    "Age": [21, 22, 20, np.nan, 24, 21],
    "Marks": [85, 90, np.nan, 78, 88, 65],
    "City": ["Delhi", "Jaipur", "Delhi", "Mumbai", np.nan, "Jaipur"]
}

df = pd.DataFrame(data)
print(df)
```

### Step 2: Inspect the dataset

``` python
print(df.head())
print("Shape:", df.shape)
df.info()
print(df.describe())
```

### Step 3: Identify missing values

``` python
print(df.isnull().sum())
```

### Step 4: Handle missing values

``` python
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
```

### Step 5: Filter students scoring above 75

``` python
high_scorers = df[df["Marks"] > 75]
print(high_scorers)
```

### Step 6: Save the cleaned dataset

``` python
df.to_csv("cleaned_students.csv", index=False)
```

### Step 7: Verify the cleaned dataset

``` python
print("Missing values after cleaning:")
print(df.isnull().sum())

print("Cleaned dataset:")
print(df)
```

The missing values should now be handled, and the cleaned dataset is
saved as `cleaned_students.csv`.

## 8. Useful Data-Cleaning Operations

Remove duplicate rows:

``` python
df = df.drop_duplicates()
```

Rename columns:

``` python
df = df.rename(columns={"Marks": "Score"})
```

Convert a column to a numeric data type:

``` python
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
```

`errors="coerce"` converts values that cannot be parsed into missing
values (`NaN`), which can then be handled.

Check data types:

``` python
print(df.dtypes)
```

## 9. Pandas Practice Questions

Try these without looking at the solutions:

1.  Display the first 10 rows of a dataset.
2.  Find the total number of rows and columns.
3.  Count missing values in each column.
4.  Replace missing `Age` values with the median.
5.  Remove duplicate rows.
6.  Filter students whose marks are greater than 85.
7.  Find students whose age is between 20 and 23.
8.  Filter students belonging to Delhi or Mumbai.
9.  Display only `Name` and `Marks` for students scoring above 80.
10. Clean a dataset and save it as a new CSV file.

## 10. Pandas Quick Revision

  Function / Attribute     Purpose
  ------------------------ ---------------------------
  `pd.read_csv()`          Load a CSV file
  `pd.DataFrame()`         Create a DataFrame
  `df.head()`              Display first rows
  `df.info()`              Inspect dataset structure
  `df.describe()`          Get statistical summary
  `df.isnull().sum()`      Count missing values
  `df.dropna()`            Remove missing records
  `df.fillna()`            Replace missing values
  `df.drop_duplicates()`   Remove duplicate rows
  `df.loc[]`               Select rows and columns
  `df.to_csv()`            Save a DataFrame as CSV



------------------------------------------------------------------------

