import pandas as pd

def analizar_columna(df, nombre_columna):
    """
    Calcula el recuento absoluto, el porcentaje y muestra todas las filas 
    de una columna dada sin truncar.
    """
    conteo = df[nombre_columna].value_counts(dropna=False)
    porcentaje = round(df[nombre_columna].value_counts(normalize=True, dropna=False) * 100, 2)
    
    df_resumen = pd.DataFrame({
        'Cantidad': conteo, 
        'Porcentaje (%)': porcentaje
    })
    
    pd.set_option('display.max_rows', None)
    return df_resumen