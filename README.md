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


# Como usar o Spark e Pyspark

1. Execute o container:
sudo docker-compose up

2. Entre no Container:
docker exec -it spark-master bash

3. Check a versão do Spark:
spark-submit --version

4. Instale na sua máquina local o virtualenv e crie uma env
virtualenv --python=python3.11 env

5. Acesse a virtualenv:
source env/bin/activate

6. instale o Pyspark relacionado a versão do Spark:
pip install pyspark==3.5.2

ou 

pip install -r requirements.txt






Contexto: Uso de PySpark para Processamento de Dados no Cluster Spark

O PySpark é a interface Python para o Apache Spark e permite que você escreva programas de análise de dados em Python enquanto aproveita o poder do processamento distribuído do Spark.

Objetivo do PySpark:
Utilizar o Cluster do Spark, que consiste em um conjunto de máquinas (chamadas de workers), para realizar transformações e análises de dados de forma distribuída e paralela.
Isso resulta em maior velocidade e eficiência no processamento de grandes volumes de dados.
Como funciona:
O PySpark fornece APIs que permitem manipular e processar dados em estruturas distribuídas, como RDDs (Resilient Distributed Datasets) ou DataFrames.
Quando você usa uma função ou método do PySpark, como .map() ou .select(), essas operações são traduzidas em jobs e enviados ao cluster para serem executados nos workers.
O driver (seu script principal) coordena essas tarefas, mas o trabalho pesado ocorre nos workers.
Sobre pipelines e funções Python:
Algumas vezes, as transformações desejadas nos dados podem ser muito específicas ou não diretamente suportadas pelas funções nativas do PySpark.
Nesse caso, você pode definir funções personalizadas em Python para realizar essas transformações.
Essas funções podem ser aplicadas nos dados usando métodos como .map(), .apply() ou UDFs (User Defined Functions) no contexto do PySpark.
Por que usar funções e o apply no PySpark?
Quando usamos o apply (ou funções equivalentes), estamos distribuindo a execução de nossas transformações para os workers do cluster.
Isso permite que cada worker processe sua parte dos dados de forma eficiente e em paralelo, em vez de realizar todo o trabalho no driver, o que seria mais lento e centralizado.














## PySpark Client
- Um ambiente interativo baseado em **Jupyter Notebook** para escrever e testar códigos PySpark.
- Ele se conecta ao Master Spark através do endereço: `spark://spark-master:7077`.
- Interface Web (Jupyter Notebook) disponível em: [http://localhost:8888](http://localhost:8888).
- Ao acessar a interface do Jupyter, ele irá pedir um Token, você terá que entrar no container que está rodando o pyspark notebook

```bash
docker exec -it pyspark-client bash
```
- Após entrar no container, digite:

```bash
jupyter server list
```
- Copie o TOKEN que aparece no resultado.
- Volte pra inteface do Jupyter e cole o Token
- Pronto, você pode usar o jupyter normalmente.


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