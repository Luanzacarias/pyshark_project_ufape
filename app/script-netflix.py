from pyspark.sql import SparkSession
import time

spark = (SparkSession.builder
    .appName("Netfllix_Titles")
    .master("spark://spark-master:7077")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

print("=== Carregando dados ===")
df = spark.read.option("header", True).csv("/dados/netflix_titles.csv")

print("=== Schema do DataFrame ===")
df.printSchema()

print("=== Primeiras linhas ===")
df.show(5)

print("=== Contagem por Categoria ===")
start = time.time()
grouped_df = df.groupBy("type").count()
grouped_df.show()
end = time.time()
print(f"Tempo de execução (groupBy): {end - start:.2f} segundos")


spark.stop()
