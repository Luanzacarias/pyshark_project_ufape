#!/bin/bash
echo "Starting Spark job..."

SCRIPT_PATH="/app/script.py"

CONTAINER_NAME="spark-client"

docker exec -it "$CONTAINER_NAME" /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --executor-cores 2 \
  --executor-memory 2g \
  --total-executor-cores 6 \
  "$SCRIPT_PATH"
