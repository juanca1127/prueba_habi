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

 # Codigo para LIKES

 ```plain
 create table property_likes (
  id bigint primary key generated always as identity,
  user_id bigint references auth_user (id),
  property_id bigint references property (id),
  created_at timestamp with time zone default now()
);
```

Lo cree de esta forma siguiendo los estandares que ya se manejan en habi

● Tabla auth_user: Guarda los datos de los usuarios.

● Tabla property_likes: Relaciona a los usuarios con las propiedades que les han dado "like".
   Cada fila representa un "like" que un usuario ha dado a una propiedad.
   El índice único en (property_id, user_id) asegura que cada usuario solo pueda dar un "like" a cada propiedad.

# Ejemplos

● Inserccion Likes

 ```plain
 INSERT INTO property_likes (property_id, user_id)
VALUES (1, 10)  -- property_id = 1, user_id = 10;

```
● Eliminacion Likes
  ```plain
 DELETE FROM property_likes
 WHERE property_id = 1 AND user_id = 10;

```
● Contar likes de una propiedad
  ```plain
 SELECT COUNT(*) AS like_count
FROM property_likes
WHERE property_id = 1;

```
● Listar propiedades con la cantidad de likes
  ```plain

SELECT p.id, p.address, p.city, COUNT(pl.id) AS total_likes
FROM property p
LEFT JOIN property_likes pl ON p.id = pl.property_id
GROUP BY p.id;

```
# Diagrama

![Diagrama entidad relacion](https://github.com/juanca1127/prueba_habi/blob/master/habi.png)

# Union de la tabla LIKES

![Diagrama entidad relacion](https://github.com/juanca1127/prueba_habi/blob/main/union.png)



