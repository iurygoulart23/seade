# Databricks notebook source
# MAGIC %sh
# MAGIC ls ../downloads/sepiesp_captados.csv 

# COMMAND ----------

# MAGIC %sh
# MAGIC rm /dbfs/mnt/ADLS_Sandbox_datalakesenai/Dados_Externos/Mapa_Emprego_Industrial/sepiesp_captados.csv
# MAGIC cp ../downloads/*.csv /dbfs/mnt/ADLS_Sandbox_datalakesenai/Dados_Externos/Mapa_Emprego_Industrial/sepiesp_captados.csv

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /dbfs/mnt/ADLS_raw_datalakesenai/Dados_Externos/Seade/
