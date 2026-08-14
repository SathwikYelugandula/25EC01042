import pandas as pd
file_path = 'C:/Users/Sathwik Yelugandula/Documents/EDA/Electrical Data/MOSFET_ID_VDS.csv'
df = pd.read_csv(file_path)
print(df.head()) # the first five rows
print(df.columns) # the exact column names -- check these!
print(df.shape) # (rows, columns)
print(df.describe()) # min, max, mean of every numeric column