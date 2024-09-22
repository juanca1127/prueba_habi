import unittest
import requests

class TestMyAPI(unittest.TestCase):

    # Prueba para el endpoint '/property'
    def test_post_propertyFilter(self):
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
                                        "description": "Sin description",
                                        "year": 2002
                                    },
                                    {
                                        "address": "calle 23 #45-67r",
                                        "city": "medellin",
                                        "status": "pre_venta",
                                        "price": 210000000,
                                        "description": "Sin description",
                                        "year": 2002
                                    }
                                ]
                            }     
        # Comparamos la respuesta real con la esperada
        self.assertEqual(response.json(), expected_response)


    def test_post_property(self):
        # URL del endpoint al que se va a hacer la petición POST
        url = 'http://localhost:8000/property'
        
  
        
        # Realizamos una petición POST al endpoint con el JSON como datos
        response = requests.post(url)
        
        # Aseguramos que la respuesta tiene un código de estado 200
        self.assertEqual(response.status_code, 200)

          # Verificamos que el contenido es JSON y contiene los datos esperados
        expected_response ={
                            "total": 55,
                            "values": [
                                {
                                    "address": "diagonal 23 #28-21",
                                    "city": "medellin",
                                    "status": "comprado",
                                    "price": 270000000,
                                    "description": "Sin description",
                                    "year": 0
                                },
                                {
                                    "address": "calle 18 k 43 - 12",
                                    "city": "cali",
                                    "status": "comprando",
                                    "price": 125000000,
                                    "description": "Sin description",
                                    "year": 0
                                },
                                {
                                    "address": "calle 23 #45-67",
                                    "city": "bogota",
                                    "status": "comprando",
                                    "price": 120000000,
                                    "description": "Hermoso apartamento en el centro de la ciudad",
                                    "year": 2000
                                },
                                {
                                    "address": "carrera 100 #15-90",
                                    "city": "bogota",
                                    "status": "en_venta",
                                    "price": 350000000,
                                    "description": "Amplio apartamento en conjunto cerrado",
                                    "year": 2011
                                },
                                {
                                    "address": "carrera 100 #15-90",
                                    "city": "medellin",
                                    "status": "en_venta",
                                    "price": 325000000,
                                    "description": "Amplio apartamento en conjunto cerrado",
                                    "year": 2011
                                },
                                {
                                    "address": "Malabar entrada 2",
                                    "city": "pereira",
                                    "status": "en_venta",
                                    "price": 350000000,
                                    "description": "Casa campestre con hermosos paisajes",
                                    "year": 2021
                                },
                                {
                                    "address": "Maracay casa 24",
                                    "city": "pereira",
                                    "status": "en_venta",
                                    "price": 450000000,
                                    "description": "Casa campestre con sala de lujo tecnologica",
                                    "year": 2020
                                },
                                {
                                    "address": "diagonal 23 #28-21e",
                                    "city": "bogota",
                                    "status": "en_venta",
                                    "price": 270000000,
                                    "description": "Apartamento con hermosas vistas",
                                    "year": 2018
                                },
                                {
                                    "address": "carrera 100 #15-90e",
                                    "city": "medellin",
                                    "status": "en_venta",
                                    "price": 325000000,
                                    "description": "Amplio apartamento en conjunto cerrado",
                                    "year": 2011
                                },
                                {
                                    "address": "Entrada 8 via cerritos",
                                    "city": "pereira",
                                    "status": "en_venta",
                                    "price": 250000000,
                                    "description": "Full casa amoblada",
                                    "year": 2020
                                },
                                {
                                    "address": "Cll 1A #11B",
                                    "city": "bucaramanga",
                                    "status": "en_venta",
                                    "price": 300000000,
                                    "description": "hermoso acabado, listo para estrenar super comodo",
                                    "year": 2021
                                },
                                {
                                    "address": "calle 23 #45-67",
                                    "city": "medellin",
                                    "status": "pre_venta",
                                    "price": 210000000,
                                    "description": "Sin description",
                                    "year": 2002
                                },
                                {
                                    "address": "carrera 100 #15-90",
                                    "city": "barranquilla",
                                    "status": "pre_venta",
                                    "price": 35000000,
                                    "description": "Sin description",
                                    "year": 2015
                                },
                                {
                                    "address": "calle 95 # 78 - 49",
                                    "city": "bogota",
                                    "status": "pre_venta",
                                    "price": 120000000,
                                    "description": "hermoso acabado, listo para estrenar",
                                    "year": 2020
                                },
                                {
                                    "address": "Entrada 3 via cerritos",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 250000000,
                                    "description": "Full casa amoblada",
                                    "year": 2020
                                },
                                {
                                    "address": "Entrada 2 via cerritos",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 270000000,
                                    "description": "Casa campestre con lago",
                                    "year": 2021
                                },
                                {
                                    "address": "M1 C5 Panorama",
                                    "city": "dosquebradas",
                                    "status": "pre_venta",
                                    "price": 290000000,
                                    "description": "Casa con entrada al centro comercial",
                                    "year": 2017
                                },
                                {
                                    "address": "Bloque 5 C26 Umbras",
                                    "city": "belen de umbria",
                                    "status": "pre_venta",
                                    "price": 120000000,
                                    "description": "Casa con entrada al centro comercial",
                                    "year": 2000
                                },
                                {
                                    "address": "calle 23 #45-67q",
                                    "city": "bogota",
                                    "status": "pre_venta",
                                    "price": 120000000,
                                    "description": "Hermoso apartamento en el centro de la ciudad",
                                    "year": 2000
                                },
                                {
                                    "address": "carrera 100 #15-90w",
                                    "city": "bogota",
                                    "status": "pre_venta",
                                    "price": 350000000,
                                    "description": "Amplio apartamento en conjunto cerrado",
                                    "year": 2011
                                },
                                {
                                    "address": "carrera 100 #15-90w",
                                    "city": "bogota",
                                    "status": "pre_venta",
                                    "price": 350000000,
                                    "description": "Amplio apartamento en conjunto cerrado",
                                    "year": 2011
                                },
                                {
                                    "address": "carrera 100 #15-90w",
                                    "city": "bogota",
                                    "status": "pre_venta",
                                    "price": 350000000,
                                    "description": "Amplio apartamento en conjunto cerrado",
                                    "year": 2011
                                },
                                {
                                    "address": "calle 23 #45-67r",
                                    "city": "medellin",
                                    "status": "pre_venta",
                                    "price": 210000000,
                                    "description": "Sin description",
                                    "year": 2002
                                },
                                {
                                    "address": "diagonal 23 #28-21s",
                                    "city": "medellin",
                                    "status": "pre_venta",
                                    "price": 270000000,
                                    "description": "Sin description",
                                    "year": 0
                                },
                                {
                                    "address": "carrera 22 #34-96v",
                                    "city": "manizales",
                                    "status": "pre_venta",
                                    "price": 39483059,
                                    "description": "Sin description",
                                    "year": 1800
                                },
                                {
                                    "address": "calle 95 # 78 - 123",
                                    "city": "bogota",
                                    "status": "pre_venta",
                                    "price": 120000000,
                                    "description": "hermoso acabado, listo para estrenar",
                                    "year": 2020
                                },
                                {
                                    "address": "calle 18 k 43 - 12e",
                                    "city": "cali",
                                    "status": "pre_venta",
                                    "price": 125000000,
                                    "description": "Sin description",
                                    "year": 0
                                },
                                {
                                    "address": "Cll 1A #11B-20v",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 300000000,
                                    "description": "hermoso acabado, listo para estrenar super comodo",
                                    "year": 2016
                                },
                                {
                                    "address": "Malabar entrada 2v",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 350000000,
                                    "description": "Casa campestre con hermosos paisajes",
                                    "year": 2021
                                },
                                {
                                    "address": "Maracay casa 24c",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 450000000,
                                    "description": "Casa campestre con sala de lujo tecnologica",
                                    "year": 2020
                                },
                                {
                                    "address": "Entrada 4 via cerritos",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 250000000,
                                    "description": "Full casa amoblada",
                                    "year": 2020
                                },
                                {
                                    "address": "Entrada 5 via cerritos",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 270000000,
                                    "description": "Casa campestre con lago",
                                    "year": 2021
                                },
                                {
                                    "address": "M8 C6 Panorama",
                                    "city": "dosquebradas",
                                    "status": "pre_venta",
                                    "price": 290000000,
                                    "description": "Casa con entrada al centro comercial",
                                    "year": 2017
                                },
                                {
                                    "address": "Bloque 5 C67 Umbras",
                                    "city": "belen de umbria",
                                    "status": "pre_venta",
                                    "price": 120000000,
                                    "description": "Casa con entrada al centro comercial",
                                    "year": 2000
                                },
                                {
                                    "address": "Cll 1A #11B-234",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 300000000,
                                    "description": "hermoso acabado, listo para estrenar super comodo",
                                    "year": 2019
                                },
                                {
                                    "address": "Maracay casa 567c",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 450000000,
                                    "description": "Casa campestre con sala de lujo tecnologica",
                                    "year": 2020
                                },
                                {
                                    "address": "Entrada 9 via cerritos",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 270000000,
                                    "description": "Casa campestre con lago",
                                    "year": 2021
                                },
                                {
                                    "address": "Bloque 53 C674 Umbras",
                                    "city": "belen de umbria",
                                    "status": "pre_venta",
                                    "price": 120000000,
                                    "description": "Casa con entrada al centro comercial",
                                    "year": 2000
                                },
                                {
                                    "address": "calle 18 k 43",
                                    "city": "cali",
                                    "status": "pre_venta",
                                    "price": 125000000,
                                    "description": "Sin description",
                                    "year": 0
                                },
                                {
                                    "address": "Cll 1A #20b",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 300000000,
                                    "description": "hermoso acabado, listo para estrenar super comodo",
                                    "year": 2020
                                },
                                {
                                    "address": "casa 24c",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 450000000,
                                    "description": "Casa campestre con sala de lujo tecnologica",
                                    "year": 2020
                                },
                                {
                                    "address": "via cerritos",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 250000000,
                                    "description": "Full casa amoblada",
                                    "year": 2020
                                },
                                {
                                    "address": "5 via cerritos",
                                    "city": "pereira",
                                    "status": "pre_venta",
                                    "price": 270000000,
                                    "description": "Casa campestre con lago",
                                    "year": 2020
                                },
                                {
                                    "address": "C67 Umbras",
                                    "city": "belen de umbria",
                                    "status": "pre_venta",
                                    "price": 120000000,
                                    "description": "Casa con entrada al centro comercial",
                                    "year": 2020
                                },
                                {
                                    "address": "Cra 11 A No 18 E 11",
                                    "city": "la virginia",
                                    "status": "pre_venta",
                                    "price": 90000000,
                                    "description": "Hermosa casa con 3 piezas",
                                    "year": 2022
                                },
                                {
                                    "address": "diagonal 23 #28-21",
                                    "city": "bogota",
                                    "status": "vendido",
                                    "price": 270000000,
                                    "description": "Apartamento con hermosas vistas",
                                    "year": 2018
                                },
                                {
                                    "address": "Cll 1A #11B-20",
                                    "city": "pereira",
                                    "status": "vendido",
                                    "price": 300000000,
                                    "description": "hermoso acabado, listo para estrenar super comodo",
                                    "year": 2019
                                },
                                {
                                    "address": "carrera 100 #15-90x",
                                    "city": "barranquilla",
                                    "status": "vendido",
                                    "price": 35000000,
                                    "description": "Sin description",
                                    "year": 2015
                                },
                                {
                                    "address": "Cll 1A #11B-20b",
                                    "city": "pereira",
                                    "status": "vendido",
                                    "price": 300000000,
                                    "description": "hermoso acabado, listo para estrenar super comodo",
                                    "year": 2019
                                },
                                {
                                    "address": "Cll 1A #11B-123",
                                    "city": "pereira",
                                    "status": "vendido",
                                    "price": 300000000,
                                    "description": "hermoso acabado, listo para estrenar super comodo",
                                    "year": 2016
                                },
                                {
                                    "address": "Malabar entrada 345",
                                    "city": "pereira",
                                    "status": "vendido",
                                    "price": 350000000,
                                    "description": "Casa campestre con hermosos paisajes",
                                    "year": 2021
                                },
                                {
                                    "address": "M8 C634 Panorama",
                                    "city": "dosquebradas",
                                    "status": "vendido",
                                    "price": 290000000,
                                    "description": "Casa con entrada al centro comercial",
                                    "year": 2017
                                },
                                {
                                    "address": "Cll 1A #11B",
                                    "city": "pereira",
                                    "status": "vendido",
                                    "price": 300000000,
                                    "description": "hermoso acabado, listo para estrenar super comodo",
                                    "year": 2020
                                },
                                {
                                    "address": "Malabar 2v",
                                    "city": "pereira",
                                    "status": "vendido",
                                    "price": 350000000,
                                    "description": "Casa campestre con hermosos paisajes",
                                    "year": 2020
                                },
                                {
                                    "address": "C6 Panorama",
                                    "city": "dosquebradas",
                                    "status": "vendido",
                                    "price": 290000000,
                                    "description": "Casa con entrada al centro comercial",
                                    "year": 2020
                                }
                            ]
                        }
        # Comparamos la respuesta real con la esperada
        self.assertEqual(response.json(), expected_response)

# Ejecución de los tests
if __name__ == '__main__':
    unittest.main()
