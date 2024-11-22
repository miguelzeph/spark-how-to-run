from pyspark.sql import SparkSession
from scripts.data_generator import generate_mock_data
from scripts.transformations import clean_column_names, filter_data

def main():
    # Criando a SparkSession
    spark = SparkSession.builder.appName("Simple PySpark Project with Mock Data").getOrCreate()

    # Gerando dados fictícios
    df = generate_mock_data(spark)

    # Aplicando transformações
    df_clean = clean_column_names(df)
    df_filtered = filter_data(df_clean)

    # Mostrando os resultados no console
    print("DataFrame Original:")
    df.show()

    print("DataFrame Filtrado (Age > 30):")
    df_filtered.show()

    # Finalizando a SparkSession
    spark.stop()

if __name__ == "__main__":
    main()
