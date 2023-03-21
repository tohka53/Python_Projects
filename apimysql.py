from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/api/customers')
def get_customers():
    # Conectar a la base de datos
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="db_prfitnessgt"
    )

    # Ejecutar la consulta
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM tb_puestos')

    # Obtener los resultados
    customers = []
    for row in cursor:
        customer = {'id_puesto': row[0], 'puesto': row[1], 'status': row[2]}
        customers.append(customer)

    # Cerrar la conexión a la base de datos
    mydb.close()

    # Devolver los resultados en formato JSON
    return jsonify(customers)

if __name__ == '__main__':
    app.run(debug=True)