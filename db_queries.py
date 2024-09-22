# db_queries.py
from db_config import connect_to_db
import pymysql
import json
from datetime import datetime

# Función para traer los inmuebles       
def get_property(Param,page,rowsPerPage):
    connection = connect_to_db()
    
    try:
        with connection.cursor() as cursor:
            offset= (int(page) -1)* int(rowsPerPage)

            #Construccion de la consulta para los inmuebles
            query= """ SELECT p.address ,p.city ,s.name as status ,p.price ,COALESCE (NULLIF(p.description,''),'Sin description') as description,
                        COALESCE(p.`year` ,0) AS 'year'
                        FROM property p
                        JOIN status_history sh on sh.property_id = p.id
                        INNER JOIN status s on sh.status_id = s.id 
                        WHERE sh.update_date =(
                        SELECT MAX(sh2.update_date)
                        FROM status_history sh2
                        WHERE sh2.property_id=p.id
                        ) AND p.address <>'' AND p.city <> '' AND p.price <>0  """
            if Param:
             # construccion de la consulta con los parametros y filtros
             query=" ".join([query,Param])
             
             # construccion de la paginacion
             pagination=" LIMIT {0} OFFSET {1}".format(rowsPerPage,offset)

             query=" ".join([query,pagination])

            
            cursor.execute(query)
            filas = cursor.fetchall()
            resultados_json = []
            columnas = [column[0] for column in cursor.description]
            for fila in filas:
                resultado = dict(zip(columnas, fila))
                for columna, valor in resultado.items():
                 if isinstance(valor, bool):  
                    continue
                 if isinstance(valor, bytes) and len(valor) == 1:  
                    resultado[columna] = bool(valor[0])  
                else:
                    resultado[columna] = valor 
                #Aqui se anidan los resultados para dar respuesta JSON 
                resultados_json.append(resultado)
   
            count = count_property(query)
            json_response = {
                   "total": count,      # Aquí el total de registros
                   "values": resultados_json}  # Aquí estarán los resultados paginados
            return json.dumps(json_response, default=serialize_datetime, indent=2)

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        connection.close()


def count_property(query):
    connection = connect_to_db()
    try:
      with connection.cursor() as cursor:
        # se reemplaza SELECT POR SELECT COUNT(*) PARA OBTENER LOS REGISTROS
        new_query = query.replace(query.split('FROM')[0], "SELECT COUNT(*) ", 1)
        
        cursor.execute(new_query)
        #Se devuelve el resultado
        total_resultados = cursor.fetchone()[0]
        return total_resultados
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        connection.close()


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError("Object of type datetime is not JSON serializable")

