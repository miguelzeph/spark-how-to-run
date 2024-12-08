# Documentation for Using Apache Spark and PySpark

## What is Apache Spark?
**Apache Spark** is a distributed data processing engine designed for large-scale data processing. It provides high speed and efficiency in transforming and analyzing distributed data.

**Purpose of Spark and PySpark:**
- **Spark:** Enables distributed and parallel processing of large datasets using a cluster of machines.
- **PySpark:** The Python interface for Spark, allowing you to build data pipelines and perform analysis using Python while leveraging distributed computing.

---

- **How it works**:
Basically the **Python script** needs to use **Spark's API**, called **PySpark**, to connect to the **Spark Cluster**, where all data transformations will take place at **high speed**.

In other words, to perform **data analysis** faster using **Spark**, we need to leverage **PySpark functions** or methods, which send messages to the **Spark WORKERS**. 

However, sometimes we have **very specific pipelines**, so we must create **Python functions** for the transformations we want to perform and apply them using **PySpark's `.apply()` method**. This ensures the data is processed **faster** on the **microserver** running **Apache Spark**. 

Alternatively, we can use **Spark's UDF (User Defined Function)**, which essentially **translates your custom function** into a format that **Spark can understand**.

---

## Spark Architecture

### Spark Master
- The **Master** is the **control node** in the Spark cluster.
- It distributes tasks to **Workers** and monitors their progress.
- Web interface available at: [http://localhost:8080](http://localhost:8080).

### Spark Worker
- **Workers** execute tasks sent by the Master.
- Each Worker has its own web interface, or we can configure all Workers to share the same port, which the **Master** will orchestrate. In this example, we created **2 Workers**, one on port `8081` and the other on `8082`:
  - [http://localhost:8081](http://localhost:8081) (Worker 1)
  - [http://localhost:8082](http://localhost:8082) (Worker 2)

---

## Setting Up Spark and PySpark Environment

1. **Start the environment with Docker Compose:**
   ```bash
   sudo docker-compose up
   ```

2. **Access the Master container:**
   ```bash
   docker exec -it spark-master bash
   ```

3. **Check the installed Spark version:**
   ```bash
   spark-submit --version
   ```

4. **Create and configure a Python virtual environment locally:**
   - Install `virtualenv`:
     ```bash
     pip install virtualenv
     ```
   - Create a Python 3.11 virtual environment:
     ```bash
     virtualenv --python=python3.11 env
     ```
   - Activate the virtual environment:
     ```bash
     source env/bin/activate
     ```

5. **Install PySpark matching the Spark version (step 3):**
   - Ensure requirements are listed in the `requirements.txt` file.
   - Install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```

6. **Open Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

7. **Test the example notebooks provided.**

---

## Using PySpark with the Spark Cluster


If you prefer not to use the provided Jupyter Notebook examples, follow the steps below to connect your Python script to PySpark.

### Connecting to the Spark Cluster
The following code demonstrates how to connect to the Spark Master and execute tasks on the cluster:
```python
from pyspark.sql import SparkSession

# Connect to the Spark Master
spark = SparkSession.builder     .appName("PySparkClient")     .master("spark://localhost:7077") \  # Connection to the Master
    .getOrCreate()

# Test by creating a simple DataFrame
data = [("Alice", 28), ("Bob", 35), ("Cathy", 30)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
```

### Benefits of PySpark
- Enables data transformations and analysis using Python on distributed structures such as:
  - **RDDs** (Resilient Distributed Datasets)
  - **DataFrames**
- Supports **custom functions** using Python for specific transformations:
  - Methods like `.map()`, `.apply()`, or UDFs (User Defined Functions).
- Distributes tasks to Workers in the cluster, ensuring efficiency and parallelism.

---

## Configuring the PySpark Client

The **PySpark Client** is an interactive environment based on **Jupyter Notebook** for writing and testing PySpark code.

### Accessing the PySpark Client's Jupyter Notebook
1. **Access the PySpark Client container:**
   ```bash
   docker exec -it pyspark-client bash
   ```

2. **Find the Jupyter Server token:**
   ```bash
   jupyter server list
   ```

3. **Access the Jupyter Notebook interface:**
   - URL: [http://localhost:8888](http://localhost:8888)
   - Paste the token from the terminal to log in.

### Example Usage in Jupyter Notebook
Within Jupyter Notebook, you can test transformations and analyses using PySpark while connected to the cluster.

---

## Running PySpark Scripts in Pipelines

To integrate Spark into pipelines (e.g., with Airflow), ensure that the Spark cluster is active. Example:

```python
from pyspark.sql import SparkSession

# Connect to the Spark Cluster
spark = SparkSession.builder     .appName("PipelineExample")     .master("spark://localhost:7077") \  # Connection to the Master
    .getOrCreate()

# Example: Process a simple DataFrame
data = [("John", 32), ("Anna", 25), ("Mike", 40)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
```

**Note:** Ensure all scripts correctly connect to the **Spark Master** using the address `spark://spark-master:7077`.

---
