import pandas as pd
import numpy as np
import os

file_path = os.getcwd() + '/data/csv/bank.csv'

data = pd.read_csv(file_path,header=0)

print('Data Types')
print(data.dtypes)
print('---------------------------------------------')


# data = data[data['y']==0]
data = data.filter(data['y'] > 0)

col_count = len(data.columns)
row_count = len(data)

print(f'Rows: {row_count}')
print(f'Columns: {col_count}')
# List all column values
for record in data.columns:
    print(f'Column Name: {record} : {data[record].unique()}')








