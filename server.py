# server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer
from db_queries import get_property
import json


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar encabezados CORS
        self.send_header('Access-Control-Allow-Origin', '*')  # Permitir todos los orígenes
        self.send_header('Access-Control-Allow-Methods', ' POST')  # Métodos permitidos
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Encabezados permitidos
        SimpleHTTPRequestHandler.end_headers(self)
    def do_POST(self):
        
        if self.path == '/property':
            # Obtener la longitud del contenido (Content-Length)
            content_length = int(self.headers['Content-Length'])
            # Se valida que no venga vacio
            if(content_length >0):
                body = self.rfile.read(content_length).decode('utf-8')
                try:

                 data = json.loads(body)
                except json.JSONDecodeError as e:
                     self.send_response(400)
                     self.send_header('Content-type', 'application/json')
                     self.end_headers()
                     # Creas un diccionario con el error
                     mensaje = json.dumps({
                        "error": str(e)  # Convertir el error a cadena si no lo es
                        })
                     # se le devuelve en JSON la respuesta
                     self.wfile.write( mensaje.encode())

            else:
                data = {}     
            Query =""
            page=1
            rowsPerPage=10
            
            #se extrae los datos que viene del body
            if data.get("page"):
                 page= int(data['page'])
            if data.get("rowsPerPage"):
                 rowsPerPage= int(data['rowsPerPage'])


            if data.get("city"):
                Qparam =f" AND p.city = '{data['city']}'"
                Query=" ".join([Query,Qparam]) # se usa para unir la consulta con los parametros

            if data.get("year"):
                Qparam =f" AND p.year = '{data['year']}'"
                Query=" ".join([Query,Qparam])

            if data.get("status"):
                Qparam =f" AND s.name = '{data['status']}'"
                Query=" ".join([Query,Qparam])
                
            
            # se le pasa los pararmetros a la funcion y se le asigna a la variable
            json_response = get_property(Query,page,rowsPerPage) 
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # se le devuelve en JSON la respuesta
            self.wfile.write( json_response.encode())
        else:
            # si no se encuentra el path devuelve 404
            self.send_error(404, "Page Not Found")

    
    

if __name__ == "__main__":
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f"Servidor corriendo en el puerto {port}")
    httpd.serve_forever()
