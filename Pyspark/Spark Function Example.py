from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("SparkFunction").getOrCreate()

# DataFrame Operations
# 1. Select 
# 2. filter
# 3. group
# 4. agg


df = spark.createDataFrame([(1, "a"), (2, "b")], ["num", "char"])
result = len(df.select("num").collect())

print(f'Applying Select resulting rows: {result}')

result = len(df.filter(df.char == 'z').collect())

print(f'Applying filter resulting rows: {result}')

result = len(df.groupBy("num").count().collect())

print(f'Applying groupBy resulting rows: {result}')


print(f'Joining two data frame')
df1 = spark.createDataFrame([(1, "a"), (2, "b")], ["num", "char"])
df2 = spark.createDataFrame([(1, "x"), (2, "y")], ["num", "char2"])
result = len(df1.select("num").collect())
print(f'data frame (df1) rows: {result}')
result = len(df2.select("num").collect())
print(f'data frame (df2) rows: {result}')
result = len(df1.join(df2, df1.num == df2.num).collect())
print(f'Applying Join resulting rows: {result}')
