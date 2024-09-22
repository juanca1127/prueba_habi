# prueba_habi
proyecto para habi

# Tecnologias
Para esta prueba solo se uso python y SimpleHTTPRequestHandler
Me base en servicios aws lambda que ya habia desarrollado antiguamente para crear logica de las consultas
con la diferencia que los dividi en varios archivos, uno para las rutas, otros conexion a DB y otro funciones y consultas

# Requermientos
Servicio de consulta
● Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y “vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).
● Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.
● Los usuarios pueden aplicar varios filtros en la misma consulta.
● Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
Estado, Precio de venta y Descripción.

# Dudas
 ● en el requerimeinto se plantea que el usuario pueda filtrar por años pero tambien dice que datos puede ver el usuario al consultar el servicio
"año de construccion","ciudad","estado" y no estaba plasmado el año, entonces decidi mosntrar "año de construccion" entre los datos para que el usuario pueda filtrar

 ● luego tuve que crear una consulta muy especifica para mostrar el ultimo valor de estado para un inmueble que seria el estado actual, fue una muy buena jugada
me gustan los retos asi 

 ● en la parte de agregar los me gusta no fue tan dificil ya que la DB se encuentra bien estructurada en cuanto las tablas y sus referencia y solo fue crear el diagrama de la tabla y referenciarla
