# Explicação Geral

## Spark Master
- O Master é o **nó de controle** no cluster Spark.
- Ele distribui tarefas para os Workers e monitora o progresso.
- Interface Web (UI) disponível em: [http://localhost:8080](http://localhost:8080).

---

## Spark Worker
- Os Workers são responsáveis por **executar as tarefas** enviadas pelo Master.
- Cada Worker possui sua própria interface Web (UI), disponível na porta `8081`:
  - [http://localhost:8081](http://localhost:8081) (Worker 1, por exemplo).

---

## PySpark Client
- Um ambiente interativo baseado em **Jupyter Notebook** para escrever e testar códigos PySpark.
- Ele se conecta ao Master Spark através do endereço: `spark://spark-master:7077`.
- Interface Web (Jupyter Notebook) disponível em: [http://localhost:8888](http://localhost:8888).



## Rodando Scripts PySpark

Caso você queira criar um pipeline, por exemplo, imagine que você tem um Airflow que é um orquestrador de pipelines, ou seja, executa os scripts para você. Você tem que ter o CLUSTER SPARK rodando, mas para usá-lo você precisa se conectar a ele, exemplo de código

```python
from pyspark.sql import SparkSession

# Conecte-se ao Spark Master
spark = SparkSession.builder \
    .appName("PySparkClient") \
    .master("spark://localhost:7077") \ # AQUI QUE SE CONECTA!!!
    .getOrCreate()

# Teste criando um DataFrame simples
data = [("Alice", 28), ("Bob", 35), ("Cathy", 30)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
```