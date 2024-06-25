# pip install pandas pyarrow

import pandas as pd
import os

# Define the folder containing Parquet files
folder_path = os.getcwd() + '/data/parquet/sample'

# List all Parquet files in the folder
parquet_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.parquet')]

# Read all Parquet files into a single DataFrame
df_list = [pd.read_parquet(file) for file in parquet_files]
combined_df = pd.concat(df_list, ignore_index=True)

# Display the combined DataFrame
print(combined_df)
