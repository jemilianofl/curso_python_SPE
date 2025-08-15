#==================================================================== 
# MÓDULO 6: LIBRERÍAS EXTERNAS Y APLICACIONES EN MACHINE LEARNING 
# ====================================================================
# -------------------------------------------------------------------- 
# 1 NUMPY Y PANDAS: LA BASE DEL ANÁLISIS DE DATOS
# -------------------------------------------------------------------- 
# NumPy (Numerical Python)
# NumPy es la librería fundamental para la computación numérica en Python. 
# Proporciona un objeto array que es mucho más rápido y flexible que las listas 
# de Python para realizar operaciones matemáticas.

import numpy as np
import time
import matplotlib.pyplot as plt

# Crear un array en NumPy
datos_pozo = np.array([150.0, 155.5, 160.2, 158.0, 165.7])
print(f"Array de datos: {datos_pozo}")
print(type(datos_pozo))
print(type([150.0, 155.5, 160.2, 158.0, 165.7]))

def suma_matrices_vanilla(matriz_a, matriz_b):
    """Suma dos matrices usando listas de Python."""
    filas = len(matriz_a)
    cols = len(matriz_a[0])
    
    matriz_resultado = [[0 for _ in range(cols)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(cols):
            matriz_resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]
            
    return matriz_resultado

def suma_matrices_numpy(matriz_a, matriz_b):
    """Suma dos matrices usando NumPy."""
    return matriz_a + matriz_b

""" # Definimos el tamaño de la matriz
tamano = 5000

print(f"Creando matrices de {tamano}x{tamano}...")

# Creamos matrices aleatorias para la prueba en formato vanilla
matriz_a_vanilla = [[i * j for j in range(tamano)] for i in range(tamano)]
matriz_b_vanilla = [[i + j for j in range(tamano)] for i in range(tamano)]

# Creamos matrices equivalentes en formato NumPy
matriz_a_np = np.array(matriz_a_vanilla)
matriz_b_np = np.array(matriz_b_vanilla)

# --- Medimos el tiempo con Python Vanilla ---
print("\n--- Suma con Python Vanilla ---")
inicio_vanilla = time.time()
suma_matrices_vanilla(matriz_a_vanilla, matriz_b_vanilla)
fin_vanilla = time.time()
tiempo_vanilla_grande = fin_vanilla - inicio_vanilla
print(f"Tiempo de ejecución: {tiempo_vanilla_grande:.4f} segundos")


# --- Medimos el tiempo con NumPy ---
print("\n--- Suma con NumPy ---")
inicio_numpy = time.time()
suma_matrices_numpy(matriz_a_np, matriz_b_np)
fin_numpy = time.time()
tiempo_numpy_grande = fin_numpy - inicio_numpy
print(f"Tiempo de ejecución: {tiempo_numpy_grande:.4f} segundos")

print(f"\nNumPy fue aproximadamente {tiempo_vanilla_grande / tiempo_numpy_grande:.0f} veces más rápido para este tamaño de matriz.")

# --- Visualización de los resultados ---
plt.figure(figsize=(8, 6))
tiempos = [tiempo_vanilla_grande, tiempo_numpy_grande]
etiquetas = ['Python Vanilla', 'NumPy']

plt.bar(etiquetas, tiempos, color=['skyblue', 'lightgreen'])
plt.title('Comparación de Tiempo de Suma de Matrices')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.show() """

""" # Pandas y Polars
# Pandas es la librería ideal para manejar y analizar datos tabulares (similares a una hoja de cálculo). 
# Su estructura de datos principal es el DataFrame, que te permite organizar datos en filas y columnas 
# con etiquetas.

import pandas as pd
import polars as pl

datos = {
    'profundidad_m': [150, 160, 170, 180, 190],
    'temperatura_c': [25.5, 26.1, 27.8, 29.3, 31.0]
}

df_pandas = pd.DataFrame(datos)
print(df_pandas)
print(type(df_pandas))

df_polars = pl.DataFrame(datos)
print(df_polars)
print(type(df_polars))

# Seleccionar una columna
print("\nColumna de temperaturas:")
print(df_pandas['temperatura_c'])

print("\nColumna de temperaturas:")
print(df_polars['temperatura_c'])

# Filtrar datos (con una condición)
print("\nFilas con temperatura > 28°C:")
print(df_pandas[df_pandas['temperatura_c'] > 28])

# Filtrar datos (con una condición)
print("\nFilas con temperatura > 28°C:")
print(df_polars.filter(pl.col('temperatura_c') > 28))

import lasio
import matplotlib.pyplot as plt

las = lasio.read("WLC_PETRO_COMPUTED_INPUT_1.LAS")
print(las.curves)

depth = las["DEPTH"]
GR = las["GR"]
RHOB = las["RHOB"]
NPHI = las["NPHI"]
print(depth)
print(GR)
las_df = las.df()
print(las_df.describe())

 plt.plot(GR, depth, color="green", linewidth=0.3, label="GR")
plt.gca().invert_yaxis()
plt.xlabel("Rayos Gamma (GR)")
plt.ylabel("Profundidad (m)")
plt.xlim([0, 200])
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------------------------------------------- 
# 2. USANDO MACHINE LEARNING
# -------------------------------------------------------------------- 

# Paso 1: Descargar y cargar los datos
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset en un DataFrame de Pandas
df_titanic = pd.read_csv('train.csv')

# Visualización inicial de la distribución de edades
plt.figure(figsize=(8, 6))
df_titanic['Age'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de Edades de Pasajeros')
plt.xlabel('Edad')
plt.ylabel('Número de Pasajeros')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Manejar valores nulos y codificar variables categóricas
df_titanic['Age'].fillna(df_titanic['Age'].median(), inplace=True)
df_titanic['Sex'] = df_titanic['Sex'].map({'male': 0, 'female': 1})
df_titanic.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

# La clasificación es la tarea de predecir una categoría discreta. Usaremos la Regresión Logística, 
# un algoritmo simple y efectivo.
# Paso 1: Preparar los datos y entrenar el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

X = df_titanic.drop('Survived', axis=1)
y = df_titanic['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo_clasificacion = LogisticRegression(solver='liblinear', random_state=42)
modelo_clasificacion.fit(X_train, y_train)

y_pred_clasificacion = modelo_clasificacion.predict(X_test)
precision = accuracy_score(y_test, y_pred_clasificacion)
print(f"\nPrecisión del modelo de clasificación: {precision:.2f}")

# Paso 2: Visualizar el límite de decisión (simplificado)
# Para hacer esto, graficaremos la predicción del modelo en función de una 
# de las variables más influyentes, como la Age o la Fare. Por simplicidad, 
# usemos una regresión logística con una sola característica para visualizar el límite de decisión.

# Creando un modelo simplificado para visualización
X_simple = df_titanic[['Age']].values.reshape(-1, 1)
y_simple = df_titanic['Survived']
modelo_simple = LogisticRegression(solver='liblinear', random_state=42)
modelo_simple.fit(X_simple, y_simple)

edades_grafica = np.linspace(min(df_titanic['Age']), max(df_titanic['Age']), 100).reshape(-1, 1)
predicciones_grafica = modelo_simple.predict(edades_grafica)

plt.figure(figsize=(10, 6))
plt.scatter(df_titanic['Age'], df_titanic['Survived'], color='grey', label='Datos reales')
plt.plot(edades_grafica, predicciones_grafica, color='red', linewidth=3, label='Predicción del modelo')
plt.title('Regresión Logística: Edad vs. Supervivencia')
plt.xlabel('Edad')
plt.ylabel('Sobrevivió (1) o No (0)')
plt.legend()
plt.show()

# La regresión es la tarea de predecir un valor numérico continuo. Usaremos el algoritmo de Árbol de Decisión.
# Paso 1: Preparar los datos y entrenar el modelo
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

X_reg = df_titanic.drop('Age', axis=1)
y_reg = df_titanic['Age']
X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

modelo_regresion = DecisionTreeRegressor(random_state=42)
modelo_regresion.fit(X_reg_train, y_reg_train)

y_pred_regresion = modelo_regresion.predict(X_reg_test)
mae = mean_absolute_error(y_reg_test, y_pred_regresion)
print(f"\nError Absoluto Medio (MAE) del modelo de regresión: {mae:.2f}")

# Paso 2: Visualizar las predicciones vs. valores reales
# Para entender qué tan bien lo está haciendo nuestro modelo, graficaremos las predicciones contra los valores reales. Si los puntos se agrupan cerca de una línea diagonal perfecta, # el modelo es muy preciso.
plt.figure(figsize=(10, 6))
plt.scatter(y_reg_test, y_pred_regresion, color='blue', alpha=0.6)
plt.plot([min(y_reg_test), max(y_reg_test)], [min(y_reg_test), max(y_reg_test)], 'r--')
plt.title('Valores Reales vs. Predicciones del Modelo de Regresión')
plt.xlabel('Edad Real')
plt.ylabel('Edad Predicha')
plt.show()
"""


# -------------------------------------------------------------------- 
# 3. CLUSTERING
# --------------------------------------------------------------------
import pandas as pd
# Paso 1. Lectura de los datos
df = pd.read_csv("15_9-F-11 A.csv", sep=";")

print("Columnas en el DataFrame:", df.columns)
depth_column = "Depth"

# Seleccionar las columnas relevantes
data_columns = ['GR', 'NPHI', 'RHOB', 'DT', 'RT', 'RPCELM']
data = df[data_columns]

# Paso 2: Estandarización
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Paso 3: Clustering Jerárquico y Dendograma
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

linked = linkage(scaled_data, method="ward")

plt.figure(figsize=(15, 10))
dendrogram(linked, orientation='top', distance_sort='ascending', show_leaf_counts=True, truncate_mode='lastp', p=12)
plt.title('Dendrograma de Clústeres Jerárquicos')
plt.xlabel('Índice de Muestra')
plt.ylabel('Distancia')
plt.grid(True)
plt.show()

# Paso 4: Selección de Clústeres Primarios
num_primary_clusters = 4
primary_clusters = fcluster(linked, num_primary_clusters, criterion='maxclust')
df['Primary_Cluster'] = primary_clusters

# Paso 5: Subdivisión en subclusteres
df['Overall_Sub_Cluster'] = 0
overall_sub_cluster_id = 1

num_subclusters_dict = {
    1: 3,
    2: 3,
    3: 3,
    4: 3
}

for primary_cluster in df['Primary_Cluster'].unique():
    # Selecciona los datos para el clúster primario actual
    cluster_data = df[df['Primary_Cluster'] == primary_cluster].copy()
    
    # Asegúrate de que haya suficientes puntos para el clustering
    if len(cluster_data) > 1:
        # Estandariza los datos solo de este subconjunto
        cluster_scaled_data = scaler.fit_transform(cluster_data[data_columns])
        
        # Realiza el clustering jerárquico
        cluster_linked = linkage(cluster_scaled_data, method='ward')
        
        # Obtiene el número de subclústeres para este clúster primario
        num_subclusters = num_subclusters_dict.get(primary_cluster, 3)
        
        # Asigna los subclústeres
        sub_clusters = fcluster(cluster_linked, num_subclusters, criterion='maxclust')
        
        # Asigna los resultados de vuelta al DataFrame original
        df.loc[df['Primary_Cluster'] == primary_cluster, 'Sub_Cluster'] = sub_clusters
        
        # Asignación de IDs globales para los subclústeres
        for sub_cluster in range(1, num_subclusters + 1):
            df.loc[
                (df['Primary_Cluster'] == primary_cluster) & (df['Sub_Cluster'] == sub_cluster),
                'Overall_Sub_Cluster'
            ] = overall_sub_cluster_id
            overall_sub_cluster_id += 1

print("\nConteo de registros por subclúster global:")
print(df['Overall_Sub_Cluster'].value_counts().sort_index())

# Paso 6: Visualización de los datos por clústeres
# Aquí está el código nuevo para generar el gráfico de dispersión
import seaborn as sns

plt.figure(figsize=(12, 8))
# Usamos un solo gráfico de dispersión para mostrar GR vs. DT coloreado por Overall_Sub_Cluster
plt.scatter(x=df['GR'], y=df['DT'], c=df['Overall_Sub_Cluster'], cmap='viridis', s=5, alpha=0.7)
plt.title('Dispersión de GR vs. DT coloreada por Subclúster Global')
plt.xlabel('GR')
plt.ylabel('DT')
cbar = plt.colorbar()
cbar.set_label('Overall Sub-Cluster')
plt.grid(True)
plt.show()

# También puedes usar Seaborn para una visualización más estética y legible
sns.pairplot(df, vars=['GR', 'NPHI', 'RHOB'], hue='Overall_Sub_Cluster', palette='viridis', plot_kws={'s': 5, 'alpha': 0.7})
plt.suptitle('Gráfico de pares coloreado por Subclúster Global', y=1.02)
plt.show()