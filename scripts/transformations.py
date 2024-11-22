from pyspark.sql import DataFrame

def clean_column_names(df: DataFrame) -> DataFrame:
    """Remove espaços e converte nomes de colunas para minúsculas."""
    for col in df.columns:
        df = df.withColumnRenamed(col, col.strip().lower().replace(" ", "_"))
    return df

def filter_data(df: DataFrame) -> DataFrame:
    """Filtra os registros com idade maior que 30."""
    return df.filter(df.age > 30)
