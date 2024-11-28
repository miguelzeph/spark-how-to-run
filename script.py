from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

# 1. Configurar o Spark (spark instance above - Done)
# Criar uma nova SparkSession
spark = SparkSession.builder \
    .appName("Script") \
    .master("spark://localhost:7077") \
    .getOrCreate()
# 2. Criar um DataFrame de exemplo
data = [
    (1, "Alice", 28),
    (2, "Bob", 35),
    (3, "Cathy", 29),
    (4, "David", 40)
]
columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)

# Mostrar o DataFrame original
print("DataFrame Original:")
df.show()

# 3. Criar uma função Python personalizada
def categorize_age(age):
    if age < 30:
        return "Young"
    elif 30 <= age < 40:
        return "Adult"
    else:
        return "Old"

# Converter a função Python para uma UDF (User Defined Function) do PySpark
# P.S. No PySpark, ao registrar uma função Python como uma UDF (User Defined Function),
# é necessário informar explicitamente o TIPO de dado que será retornado pela FUNÇÃO.
categorize_age_udf = udf(
    categorize_age, # função python do usuário
    StringType() # Especificando o tipo da função
)

# Aplicar a UDF ao DataFrame
df_transformed = df.withColumn(
    "age_category",
    categorize_age_udf(col("age"))
)

# Mostrar o DataFrame transformado
print("DataFrame Transformado:")
df_transformed.show()
