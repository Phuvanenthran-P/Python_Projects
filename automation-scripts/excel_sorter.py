import pandas as pd

file = input("Enter Excel file name: ")

df = pd.read_excel(file)
df_sorted = df.sort_values(by=df.columns[0])

df_sorted.to_excel("sorted.xlsx", index=False)

print("Excel sorted and saved.")
