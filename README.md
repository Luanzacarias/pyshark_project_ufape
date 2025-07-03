
# 🚀 Projeto de Análise de Dados com Apache Spark

Este projeto demonstra como executar um cluster Apache Spark com Docker e Docker Compose, realizando análise distribuída de um dataset CSV usando PySpark.

## 🏗️ Arquitetura do Projeto

- 🔹 1 Spark Master
- 🔸 3 Spark Workers
- 🟢 1 Spark Client (para execução dos scripts)

## 📂 Estrutura de Diretórios

```
.
├── app/            # Scripts em PySpark
│   └── script-netflix.py
│   └── script.py
├── dados/          # Dataset CSV
│   └── netflix_titles.csv
│   └── yellow_tripdata_2015.csv
├── docker-compose.yml
└── README.md
└── run_spark.sh
```

## ▶️ Passos para Executar

### 1️⃣ Clone o Projeto

```bash
git clone git@github.com:Luanzacarias/pyshark_project_ufape.git
cd pyshark_project_ufape
```

### 2️⃣ Adicione o Dataset

Utilizamos o arquivo "yellow_tripdata_2015-01.csv" disponível no Kaggle [aqui](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data), contém dados das viagens feitas por táxis em New York no ano de 2015 no mês de Janeiro. Além dele, ainda usamos um base de dados dos títulos dos filmes e séries da Netflix também no Kaggle, disponível [aqui](https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download)

```
dados/netflix_titles.csv ~ 3,15MB
dados/yellow_tripdata_2015-01.csv ~ 2GB
```


### 3️⃣ Suba os Containers

```bash
docker-compose up -d
```

### 4️⃣ Rode o script shell

```bash
./run_spark.sh
```

O resultado será exibido diretamente no terminal e salvo em um arquivo `metricas.txt`.

---

## 🌐 Interfaces Web

- **Spark Master UI:** [http://localhost:8080](http://localhost:8080)

Aqui você pode visualizar os workers conectados, jobs em execução e status do cluster.

---

## ⛔ Encerrando o Cluster

```bash
docker-compose down
```

---

## 🧠 Referências

- [Apache Spark Docker Hub](https://hub.docker.com/_/spark)
- [Documentação do Apache Spark](https://spark.apache.org/docs/latest/)

---
