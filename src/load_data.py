import pandas as pd

df = pd.read_csv("data/all_stocks_5yr.csv")

print("\nPrint first five rows")
print(df.head(10))

print("\nprint columns")
print(df.columns)

print("\nShape")
print(df.shape)

print("\nMissing values")
print(df.isnull().sum())
