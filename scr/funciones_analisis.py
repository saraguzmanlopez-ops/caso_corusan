import pandas as pd

def analizar_columna(df, nombre_columna):
    """
    Calcula el recuento absoluto, el porcentaje y muestra todas las filas 
    de una columna dada sin truncar.
    """
    conteo = df[nombre_columna].value_counts(dropna=False)
    porcentaje = round(df[nombre_columna].value_counts(normalize=True, dropna=False) * 100, 2)
    
   

def limpiar_ciudades(df, nombre_columna='Localización Ciudad'):
    """
    Estandariza los nombres de las ciudades:
    1. Convierte todo a minúsculas y elimina espacios en blanco sobrantes.
    2. Elimina las tildes de las vocales para unificar variantes (ej. Málaga -> malaga).
    """
    df_limpio = df.copy()
    
    if nombre_columna in df_limpio.columns:
        def procesar_texto(valor):
            if pd.isna(valor):
                return valor
            # 1. Pasar a minúsculas y quitar espacios en los extremos
            texto = str(valor).strip().lower()
            
            # 2. Reemplazar vocales con tilde para unificar
            tildes = {
                'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u',
                'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u'
            }
            for con_tilde, sin_tilde in tildes.items():
                texto = texto.replace(con_tilde, sin_tilde)
                
            return texto
            
        df_limpio[nombre_columna] = df_limpio[nombre_columna].apply(procesar_texto)
        print(f"¡Columna '{nombre_columna}' normalizada a minúsculas y sin tildes con éxito!")
    else:
        print(f"Aviso: La columna '{nombre_columna}' no se encuentra en el DataFrame.")
        
    return df_limpio