# install library if found missing
# pip install pyspark
import os
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ParquetLoader").getOrCreate()

# Define the folder containing Parquet files
folder_path = os.getcwd() + '/data/parquet/sample'

# Read the folder of Parquet files into a Spark DataFrame
df = spark.read.parquet(folder_path)

# Show the contents of the DataFrame
df.show()

# If needed, convert the Spark DataFrame to a Pandas DataFrame
pandas_df = df.toPandas()

# Display the Pandas DataFrame
print(pandas_df)
