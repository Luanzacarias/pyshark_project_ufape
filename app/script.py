from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    countDistinct, avg, sum as sum_, hour, to_timestamp, col, when
)
import time
import os
import sys

log_path = "/dados/metricas.txt"
os.makedirs(os.path.dirname(log_path), exist_ok=True)
log_file = open(log_path, "w")

class Tee:
    def __init__(self, *streams):
        self.streams = streams
    def write(self, data):
        for s in self.streams:
            s.write(data)
    def flush(self):
        for s in self.streams:
            s.flush()

tee = Tee(sys.stdout, log_file)
sys.stdout = tee
sys.stderr = tee

spark = (SparkSession.builder
    .appName("NYC_Taxi_Metrics")
    .master("spark://spark-master:7077")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

def print_section(title):
    print("\n" + "="*40)
    print(f"  {title}")
    print("="*40)


print_section("01 - Carregando dados")
df = (spark.read
      .option("header", True)
      .option("inferSchema", True)
      .csv("/dados/yellow_tripdata_2015-01.csv")
)

print_section("02 - Esquema do DataFrame")
df.printSchema()

print_section("03 - Primeiras 5 linhas")
df.show(5, truncate=False)

print_section("04 - Estatísticas descritivas")
df.select("trip_distance", "fare_amount", "tip_amount", "passenger_count") \
  .describe() \
  .show()

print_section("05 - Métricas agregadas")
start = time.time()

df_valid = df.filter(col("fare_amount") > 0)

total_trips    = df.count()
unique_vendors = df.select(countDistinct("VendorID")).collect()[0][0]
total_revenue  = df.agg(sum_("total_amount").alias("total_revenue")).collect()[0][0]
avg_distance   = df.agg(avg("trip_distance").alias("avg_distance")).collect()[0][0]
avg_fare       = df_valid.agg(avg("fare_amount").alias("avg_fare")).collect()[0][0]

df_pct = df.withColumn(
    "tip_pct",
    when(col("fare_amount") != 0, col("tip_amount")/col("fare_amount")*100)
)
avg_tip_pct    = df_pct.agg(avg("tip_pct").alias("avg_tip_pct")).collect()[0][0]

elapsed = time.time() - start

print(f" • Total de viagens:       {total_trips:,}")
print(f" • Fornecedores distintos: {unique_vendors}")
print(f" • Receita total (USD):    {total_revenue:,.2f}")
print(f" • Distância média (mi):   {avg_distance:.2f}")
print(f" • Tarifa média (USD):     {avg_fare:.2f}")
print(f" • % Gorjeta média:        {avg_tip_pct:.1f}%")
print(f" ** Tempo de agregações:   {elapsed:.2f} segundos")


print_section("06 - Viagens por tipo de pagamento")
df.groupBy("payment_type") \
  .count() \
  .orderBy("count", ascending=False) \
  .show(truncate=False)


print_section("07 - Viagens por hora do dia")
df2 = df.withColumn("pickup_hour", hour(to_timestamp("tpep_pickup_datetime")))
df2.groupBy("pickup_hour") \
   .count() \
   .orderBy("pickup_hour") \
   .show(24, False)

spark.stop()

# Fecha o arquivo de log
log_file.close()
