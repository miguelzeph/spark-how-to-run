from pyspark.sql import SparkSession

def generate_mock_data(spark: SparkSession):
    """Gera dados fictícios para testes."""
    data = [
        ("Alice", 29),
        ("Bob", 35),
        ("Cathy", 41),
        ("David", 25),
        ("Eva", 32)
    ]
    columns = ["Name", "Age"]
    return spark.createDataFrame(data, columns)
