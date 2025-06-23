
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
│   └── script.py
├── dados/          # Dataset CSV
│   └── exemplo.csv
├── docker-compose.yml
└── README.md
```

## ▶️ Passos para Executar

### 1️⃣ Clone o Projeto

```bash
git clone git@github.com:Luanzacarias/pyshark_project_ufape.git
cd pyshark_project_ufape
```

### 2️⃣ Adicione seu Dataset

Coloque seu arquivo CSV dentro da pasta `/dados`. Exemplo:

```
dados/exemplo.csv
```

### 3️⃣ Suba os Containers

```bash
docker-compose up -d
```

### 4️⃣ Acesse o Container Cliente

```bash
docker exec -it <container-id:spark-client> bash
```

### 5️⃣ Execute seu Script PySpark

```bash
/opt/spark/bin/spark-submit /app/script.py
```

O resultado será exibido diretamente no terminal.

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
