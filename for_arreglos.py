from statistics import LinearRegression
import cx_Oracle
import mysql.connector
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Conectar a la base de datos de Oracle
#conn = cx_Oracle.connect('user/password@host:port/service')
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='db_personal_record')
# Obtener los datos necesarios para hacer la predicción desde la base de datos de Oracle
query = "SELECT nombre_completo, email, numero_telefonico FROM tb_clientes"
df = pd.read_sql(query, con=cnx)

# Preprocesar los datos
# ...

# Entrenar un modelo de regresión lineal utilizando los datos preprocesados
X = df[['email', 'numero_telefonico']]
y = df['nombre_completo']
model = LinearRegression().fit(X, y)

# Utilizar el modelo entrenado para hacer predicciones en nuevos datos
new_data = pd.DataFrame({'email': [1, 2, 3], 'numero_telefonico': [4, 5, 6]})
predictions = model.predict(new_data)

# Guardar las predicciones en la base de datos de Oracle
# ...
