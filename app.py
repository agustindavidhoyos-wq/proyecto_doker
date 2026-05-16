import os, time
import mysql.connector
# Esperamos unos segundos a que MySQL termine de arrancar
time.sleep(15)
conn = mysql.connector.connect(
 host=os.environ['DB_HOST'],
 user=os.environ['DB_USER'],
 password=os.environ['DB_PASS'],
 database=os.environ['DB_NAME'],
)
cur = conn.cursor()
cur.execute('''
 CREATE TABLE IF NOT EXISTS alumnos (
 id INT AUTO_INCREMENT PRIMARY KEY,
 nombre VARCHAR(50) NOT NULL,
 nota DECIMAL(4,2)
 )
''')
cur.execute('INSERT INTO alumnos (nombre, nota) VALUES (%s, %s)',
 ('Ana', 9.5))
conn.commit()
cur.execute('SELECT id, nombre, nota FROM alumnos')
for fila in cur.fetchall():
 print('Fila:', fila)
cur.close(); conn.close()
print('Listo')
