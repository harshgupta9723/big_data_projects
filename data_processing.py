from distutils.sysconfig import customize_compiler
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


kafka_topic_name = 'test-topic'
kafka_bootstrap_server = 'localhost:9092'

print('Starting Spark Session')

print("hello")

spark = SparkSession \
        .builder \
        .appName("PySpark Structured Streaming with Kafka Demo") \
        .master("local[*]") \
        .config("spark.jars", "/home/harsh/Downloads//spark-sql-kafka-0-10_2.11-2.4.0.jar,/home/harsh/Downloads//kafka-clients-1.1.0.jar") \
        .config("spark.executor.extraClassPath", "/home/harsh/Downloads//spark-sql-kafka-0-10_2.11-2.4.0.jar:/home/harsh/Downloads//kafka-clients-1.1.0.jar") \
        .config("spark.executor.extraLibrary", "/home/harsh/Downloads//spark-sql-kafka-0-10_2.11-2.4.0.jar:/home/harsh/Downloads//kafka-clients-1.1.0.jar") \
        .config("spark.driver.extraClassPath", "/home/harsh/Downloads//spark-sql-kafka-0-10_2.11-2.4.0.jar:/home/harsh/Downloads//kafka-clients-1.1.0.jar") \
        .getOrCreate()
        
spark.sparkContext.setLogLevel(newLevel="ERROR")

print("hello")
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_server) \
    .option("subscribe", kafka_topic_name) \
    .option("startingOffsets", "latest") \
    .load()


print("Printing Schema of transaction_detail_df: ")
df.printSchema()



    
