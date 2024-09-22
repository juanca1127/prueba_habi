import unittest
import requests

class TestMyAPI(unittest.TestCase):

    # Prueba para el endpoint '/property'
    def test_post_property(self):
        # URL del endpoint al que se va a hacer la petición POST
        url = 'http://localhost:8000/property'
        
        # JSON que se enviará en la petición POST
        payload = {
    "page":1,
    "rowsPerPage":10,
    "status":"pre_venta",
    "city":"medellin",
    "year":2002
    
}
        
        # Realizamos una petición POST al endpoint con el JSON como datos
        response = requests.post(url, json=payload)
        
        # Aseguramos que la respuesta tiene un código de estado 200
        self.assertEqual(response.status_code, 200)

          # Verificamos que el contenido es JSON y contiene los datos esperados
        expected_response = {
                                "total": 2,
                                "values": [
                                    {
                                        "address": "calle 23 #45-67",
                                        "city": "medellin",
                                        "status": "pre_venta",
                                        "price": 210000000,
                                        "description": "",
                                        "year": 2002
                                    },
                                    {
                                        "address": "calle 23 #45-67r",
                                        "city": "medellin",
                                        "status": "pre_venta",
                                        "price": 210000000,
                                        "description": "",
                                        "year": 2002
                                    }
                                ]
                            }
        
        # Comparamos la respuesta real con la esperada
        self.assertEqual(response.json(), expected_response)

# Ejecución de los tests
if __name__ == '__main__':
    unittest.main()
