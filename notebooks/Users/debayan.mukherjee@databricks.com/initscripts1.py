# Databricks notebook source
dbutils.fs.mkdirs("dbfs:/databricks/scripts/")|

# COMMAND ----------

dbutils.fs.put("/databricks/scripts/postgresql-install.sh","""
#!/bin/bash
wget --quiet -O /mnt/driver-daemon/jars/postgresql-42.2.2.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar""", True)

# COMMAND ----------

cat dbfs:/cluster-logs/1109-175926-onq77l1d/init_scripts/1109-175926-onq77l1d_10_139_64_9/20211110_112955_00_postgresql-install.sh.stdout.log;

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /dbfs/cluster-logs/1109-175926-onq77l1d/init_scripts/1109-175926-onq77l1d_10_139_64_9/20211110_112955_00_postgresql-install.sh.stdout.log

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/scripts/postgresql-install.sh"))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/cluster-logs/1109-175926-onq77l1d/init_scripts/1109-175926-onq77l1d_10_139_64_9/20211110_112955_00_postgresql-install.sh.stdout.log"))

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /dbfs/cluster-logs/1109-175926-onq77l1d/eventlog/1109-175926-onq77l1d_10_139_64_12/6069981970363877542/eventlog

# COMMAND ----------

