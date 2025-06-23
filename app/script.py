from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Analisando Dados") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

print("=== Carregando dados ===")
df = spark.read.option("header", True).csv("/dados/exemplo.csv")

df.printSchema()

print("=== Primeiras linhas ===")
df.show(5)

print("=== Contagem por Categoria ===")
df.groupBy("categoria").count().show()

print("=== Total de registros ===")
print(df.count())

spark.stop()
