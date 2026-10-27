📊 Proyecto Integrado: 

Pipeline de Datos y Análisis Exploratorio Curasan  desarrollado para la extracción, limpieza, transformación, modelado y visualización de datos y analisis de los mismos

📑 Tabla de Contenidos

Descripción del Proyecto Objetivos y AlcanceStack 

TecnológicoEstructura del Repositorio

Arquitectura del Pipeline (ETL)

Resultados e Insights Principales

Instalación y Guía de Uso

Créditos y Autoría

📝 Descripción del Proyecto

Este proyecto aborda el ciclo de vida completo de los datos:

 desde la ingesta de conjuntos de datos heterogéneos hasta la entrega de un cuadro de mando listo para la toma de decisiones estratégicas.
 
 A lo largo del desarrollo, he trabajado de forma iterativa para garantizar la integridad de los datos, aplicar transformaciones robustas y diseñar una arquitectura limpia y modular.
 
 🎯 Objetivos y Alcance
 
 Extracción e Ingesta: Consolidar fuentes de datos crudas asegurando la trazabilidad de los datos originarios.
 
 Limpieza y Transformación (Tratamiento EDA):Detección y resolución de valores nulos, duplicados e inconsistencias de tipado.
 
 Normalización y estandarización de columnas clave.
 
 Gestión de valores atípicos (outliers) e imprecisiones del dominio.
 
 Modelado y Almacenamiento: Diseñar y estructurar la base de datos relacional para optimizar las consultas analyticals.
 
 Explotación Visual: Construir un panel interactivo que responda a preguntas de negocio concretas.
 
 🛠️ Stack Tecnológico
 
 EtapaTecnología / Librería
 
 Lenguaje principal Python 3.x,  

Manipulación Pandas, NumPy  / Matplotlib / SeabornControl de Versiones y EntornoGit, GitHub, VS Code



⚙️ Arquitectura del Pipeline 

(ETL)El flujo de trabajo se divide en 4 fases automatizadas e interconectadas: 

(Extracción): Lectura de las fuentes de origen registrando metadatos de carga.

(Transformación):Aplicación de funciones de depuración creadas a medida.

Conversión de tipos de datos y generación de nuevas variables/métricas derivadas.

Load (Carga): Inserción en la base de datos siguiendo una estructura relacional óptima.

(Visualización): Conexión del modelo analítico con el cuadro de mando final.

📈 Resultados e Insights Principales

💡 Optimización de la Calidad de Datos: Se redujo el porcentaje de inconsistencias y nulos a 0% tras el pipeline de limpieza.

💡 Descubrimiento Analítico: Identificación de patrones principales y tendencias clave en el dataset procesado.

💡 Automatización: Ejecución del pipeline modular mediante main.py, permitiendo procesar nuevos lotes de datos de forma eficiente.

🔧 Instalación y Guía de UsoClonar el repositorio:git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
Crear y activar un entorno virtual:python -m venv venv
# En Linux/macOS:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
Instalar dependencias:pip install -r requirements.txt
Ejecutar el proceso ETL:python main.py
👥 Créditos y AutoríaProyecto realizado en colaboración y trabajo en equipo.Desarrollado por: Tu NombreAsistencia y Soporte de Desarrollo: Gemini (Asistente de IA)