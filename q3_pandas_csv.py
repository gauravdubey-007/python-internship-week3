"""Q3: Use Pandas to load and analyze a CSV file."""

import os

import pandas as pd

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")
df = pd.read_csv(path)

print("First rows:")
print(df.head())
print("\nShape (rows, columns):", df.shape)
print("\nSummary of marks:")
print(df["marks"].describe())
print("\nAverage marks per student:")
print(df.groupby("name")["marks"].mean().round(2))
print("\nAverage marks per subject:")
print(df.groupby("subject")["marks"].mean().round(2))
print("\nHighest marks:")
print(df.loc[df["marks"].idxmax()])
