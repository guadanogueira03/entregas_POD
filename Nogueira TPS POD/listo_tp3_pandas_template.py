# -*- coding: utf-8 -*-
"""LISTO TP3 PANDAS - TEMPLATE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BepL7g4QVXzmFCh1TFiDkx1IiqzPAAVo

*   **Año:** [2024]
*   **Alumno/a:** [Guadalupe Nogueira]
*   **Legajo:** [1203495]

# Pandas
A continuación, cada celda va a pedir algo distinto. Por favor, realizarlo con la menor cantidad de lineas posibles y con NumPy.

Importar `pandas` con el alias `pd` e imprimir la versión instalada.
"""

import pandas as pd
print(pd. __version__)

"""Crear la siguiente tabla como un dataframe de Pandas donde cada linea represente un diccionario.

| _Index_ | **nombre**       | **edad** | **dni**  |
|---------|------------------|----------|----------|
| 9       | Brown, James     | 43       | 30123444 |
| 3       | Hamkel, Louis V. | 29       | 44555666 |
| 7       | Baptista, Carlos | 28       | 43120111 |
"""

tabla = pd.DataFrame([{"Nombre": "Brown, James","edad": 43, "dni" : 30123444},{"Nombre": "Hamkle, Louis V","edad": 29, "dni" : 44555666},{"Nombre": "Baptista, Carlos","edad": 28, "dni" : 43120111} ], index = [9,3,7])
tabla

"""Crear la siguiente tabla como un dataframe de Pandas donde todas las lineas esten dentro de un solo diccionario.

| _Index_ | **nombre**       | **edad** | **dni**  |
|---------|------------------|----------|----------|
| 9       | Brown, James     | 43       | 30123444 |
| 3       | Hamkel, Louis V. | 29       | 44555666 |
| 7       | Baptista, Carlos | 28       | 43120111 |
"""

pd.DataFrame({
    "nombre" : ["Brown,James","Hamkel,Louis V.", "Baptista, Carlos"],
    "edad" :  [43,29,28],
    "dni" :  [30123444,44555666,43120111]},
             index = [9,3,7]
             )

"""Crear la siguiente tabla como un dataframe de Pandas donde se usen unicamente listas.

| _Index_ | **nombre**       | **edad** | **dni**  |
|---------|------------------|----------|----------|
| 9       | Brown, James     | 43       | 30123444 |
| 3       | Hamkel, Louis V. | 29       | 44555666 |
| 7       | Baptista, Carlos | 28       | 43120111 |
"""

res = pd.DataFrame([["Brown, James", 43, 30123444], ["Hamjel, Louis V",29,44555666],["Baptista, Carlos",28,43120111]],
                   index = [9,3,7],
                   columns = ["nombre", "edad", "dni"]

)
res

"""Crear la siguiente tabla como un dataframe de Pandas donde se usen unicamente `Series`.

| _Index_ | **nombre**       | **edad** | **dni**  |
|---------|------------------|----------|----------|
| 9       | Brown, James     | 43       | 30123444 |
| 3       | Hamkel, Louis V. | 29       | 44555666 |
| 7       | Baptista, Carlos | 28       | 43120111 |
"""

datos = {
    "nombre": pd.Series(["Brown, James", "Hamkel, Louis V"," Baptista, Carlos"], index = [9,3,7]),
    "edad" : pd.Series([43,29,28], index = [9,3,7]),
    "dni": pd.Series([30123444,44555666,43120111], index = [9,3,7])
                            }


res = pd.DataFrame(datos)
res

"""Reutilice cualquiera de los dataframe hechos anteriormente pero agregue la columna `fecha` con el tipo de dato relacionado a fechas.

| _Index_ | **nombre**       | **edad** | **dni**  | **fecha**  |
|---------|------------------|----------|----------|------------|
| 9       | Brown, James     | 43       | 30123444 | 12/08/1981 |
| 3       | Hamkel, Louis V. | 29       | 44555666 | 10/04/1995 |
| 7       | Baptista, Carlos | 28       | 43120111 | 28/05/1996 |
"""

res['fecha'] = pd.to_datetime(['12/08/1981', '10/04/1995', '28/05/1996'], format='%d/%m/%Y')
res

"""Ejecute la siguiente celda. Se va a descargar un archivo llamado `u.user`."""

!wget https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user

"""Lea el archivo con pandas y muestre las primeras 5 filas."""

data = pd.read_csv("u.user", sep = "|")
data.head(5)

df = pd.DataFrame(data)

df.head(5)

"""Utilice la columna `user_id` como indice y saque dicha columna del dataframe


"""

df = df.set_index('user_id')
df

df.loc[2]

"""¿Cuantas categorias de trabajos hay?"""

num_categorias = df['occupation'].nunique()

print(f'Número de categorías de trabajos: {num_categorias}')

""" Reporte el porcentaje de personas que tiene cada ocupación."""

porcentaje_ocupaciones = df['occupation'].value_counts(normalize=True) * 100


print(round(porcentaje_ocupaciones,2))

"""Reporte el promedio de edad de los estudiantes usando indexeo booleano."""

edad_estudiantes = df[df['occupation'] == 'student']['age']

promedio_edad = edad_estudiantes.mean()

print('El promedio de edad de los estudiantes es:' , round(promedio_edad,2))

"""Mostrar, con una sola linea y sin importar `matplotlib`, un histograma de las edades de las personas que son administradores."""

df[df['occupation'] == 'administrator']['age'].plot(kind='hist', title='Histograma de Edades de Administradores')

"""Reemplace, sin usar `for`, en la columna `gender` `F` por `female` y `M` por `male`."""

df['gender'] = df['gender'].replace({'F': 'female', 'M': 'male'})

df

"""# Yahoo! Finance

Vamos a analizar acciones. La siguiente linea accede a Yahoo Finance y devuelve un DataFrame con los valores de la acción cada dia desde el 1980.
"""

import yfinance as yf
dataframe = yf.download('AAPL', start="1980-01-01", end="2030-01-01")

"""¿Cual es el registro mas viejo? Imprimirlo."""

viejo = dataframe.head(1)
viejo

"""Cree la columna `Average` tal que

$$Average =  \frac{High-Low}{2}$$

y muestre con un histograma dicha columna.
"""

dataframe["Average"] =(dataframe["High"]- dataframe["Low"]) / 2
dataframe["Average"].hist()

"""Con `matplotlib`, muestre como `Average` fue evolucionando *al final de cada año*."""

import matplotlib.pyplot as plt
res = dataframe.groupby(lambda x: x.year).tail(1)
res["Average"].plot()

"""Muestre con un gráfico de barras, como el volumen fue cambiando *año a año*."""

dataframe.groupby(dataframe.index.year)['Volume'].sum().plot(kind='bar')
plt.xlabel('Año')
plt.ylabel('Volumen')
plt.title('Volumen Anual')
plt.show()

"""# Cancelaciones y Delays de vuelos del 2015

Creese una cuenta en Kaggle e importe los archivos del dataset del siguiente link: https://www.kaggle.com/datasets/usdot/flight-delays. Cree los dataframes `airlines`, `airports`, y `flights` apartir de esos archivos.
"""

#Una forma de importar archivos es accediendo desde una carpeta Drive y compartiendola

#from google.colab import drive
#drive.mount('/content/drive')

#import pandas as pd
#airlines = pd.read_csv('/content/drive/My Drive/DATASETS_pandas/airlines.csv')
#airports = pd.read_csv('/content/drive/My Drive/DATASETS_pandas/airports.csv')
#flights = pd.read_csv('/content/drive/My Drive/DATASETS_pandas/flights.csv')



# Otra forma es subir los archivos al collab directo, para no tener que compartir una carpetra Drive en la entrega()

airlines = pd.read_csv("/content/airlines.csv")

airports = pd.read_csv("/content/airports.csv")

flights = pd.read_csv("/content/flights.csv")

df_airlines = pd.DataFrame(airlines)

df_airports = pd.DataFrame(airports)

df_flights = pd.DataFrame(flights)

from google.colab import drive
drive.mount('/content/drive')

"""Combine (*join*) las tablas `airlines`, `airports`, y `flights` en una sola tabla."""

df_airports.rename(columns = {"IATA_CODE" : "IATA_CODE_airports"}, inplace = True)
df_flights.rename(columns = {"AIRLINE" : "AIRLINE_flights"}, inplace = True)

df = df_flights.join(df_airports)
df = df.join(df_airlines)
df

"""¿Cuantos vuelos fueron al aeropuerto JFK?"""

conteo_jfk = (df['DESTINATION_AIRPORT'] == 'JFK').sum()
conteo_jfk

"""¿Cuantos vuelos hizo la aerolinea AA?"""

conteo_aa = (df['AIRLINE_flights'] == 'AA').sum()
conteo_aa

"""¿Que aerolineas (las primeras 5) tuvo la menor cantidad de vuelos con atrasos? Imprimirlas."""

as_retraso = ((df['DEPARTURE_DELAY'] > 0) & (df['AIRLINE_flights'] == "AS")).sum()


aa_retraso = ((df['DEPARTURE_DELAY'] > 0) & (df['AIRLINE_flights'] == "AA")).sum()


us_retraso = ((df['DEPARTURE_DELAY'] > 0) & (df['AIRLINE_flights'] == "US")).sum()


ua_retraso = ((df['DEPARTURE_DELAY'] > 0) & (df['AIRLINE_flights'] == "UA")).sum()


dl_retraso = ((df['DEPARTURE_DELAY'] > 0) & (df['AIRLINE_flights'] == "DL")).sum()


valores = [[as_retraso, "AS"], [aa_retraso, "AA"], [us_retraso, "US"], [ua_retraso, "UA"], [dl_retraso, "DL"]]
valores.sort()
res = valores[0][1]
print("La aerolinea con menor cantidad de atrasos es:", res)

"""¿Que aerolineas (las primeras 5) tuvo la mayor cantidad de vuelos con atrasos? Imprimirlas."""

res = valores[4][1]
print("La aerolinea con mayor cantidad de atrasos es:", res)

"""Haga un resumen de las razones por la cual los vuelos se atrasan."""

resumen = df['CANCELLATION_REASON'].value_counts()

print(resumen)

"""Compruebe si hay columnas con celdas vacias."""

columnas_vacias = df.isnull().any()

print(columnas_vacias[columnas_vacias == True])

"""Haga una imputación de datos COMPLETA del dataframe. Pueden escojer cualquier estrategia y no necesariamente todas las columnas deben seguir la misma estrategia."""

# Utilizo la media para columnas numericas
df.fillna(df.mean(numeric_only=True), inplace=True)

# Utilizo la moda para vriables categoricas
for col in df.select_dtypes(include='object'):
    df[col].fillna(df[col].mode()[0], inplace=True)

df