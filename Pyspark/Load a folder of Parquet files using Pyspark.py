# install library if found missing
# pip install pyspark
import os
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ParquetLoader").getOrCreate()

# Define the folder containing Parquet files
folder_path = os.getcwd() + '/data/parquet/userdata'

# Read the folder of Parquet files into a Spark DataFrame
df = spark.read.parquet(folder_path)

# Print Schema
print(df.printSchema())

# Print Statistics
print(df.describe().show())

# Show the contents of the DataFrame
#df.show()


