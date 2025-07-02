from pyspark.sql import SparkSession
import time

# Criação da sessão Spark
spark = SparkSession.builder \
    .appName("Analisando Dados") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

print("=== Carregando dados ===")
# Carregando o arquivo CSV com header
df = spark.read.option("header", True).csv("/dados/netflix_titles.csv")

# Exibindo o schema do DataFrame
df.printSchema()

print("=== Primeiras linhas ===")
df.show(5)

# ----------- Agrupamento por categoria (ou 'type' se for o nome correto no seu CSV) -----------
print("=== Contagem por Categoria ===")
start = time.time()
grouped_df = df.groupBy("type").count()
grouped_df.show()
end = time.time()
print(f"Tempo de execução (groupBy): {end - start:.2f} segundos")


# Finaliza a sessão Spark
spark.stop()
