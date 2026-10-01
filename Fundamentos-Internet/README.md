# Fundamentos de Internet #

## 1. Del Cliente al Servidor:

1. El cliente interpreta la URL:

El navegador (cliente) recibe 'www.youtube.com' y primero revisa si ya tiene esa dirección guardada en su caché local o en el archivo hosts del sistema. Si no la tiene, sabe que necesita averiguar la dirección IP asociada a ese nombre de dominio antes de poder contactar al servidor.

2. Consulta al DNS:

El navegador envía una solicitud al sistema de nombres de dominio (DNS), que funciona como una 'agenda telefónica' de internet. El DNS recorre una jerarquía de servidores (resolver local, servidores raíz, servidores TLD .com, y finalmente los servidores autoritativos de YouTube/Google) hasta traducir 'www.youtube.com' en una dirección IP numérica, por ejemplo 142.250.xxx.xxx.

3. Obtención de la dirección IP:

Con la IP en mano, el cliente ya sabe exactamente a qué máquina de la red debe dirigirse. La dirección IP identifica de forma única al servidor (o al conjunto de servidores, ya que Google usa balanceo de carga y CDNs distribuidos geográficamente) que atenderá la solicitud.

4. Se establece la conexión TCP y el cifrado TLS:

El navegador inicia una conexión TCP con esa IP mediante el 'triple apretón de manos' (SYN, SYN-ACK, ACK). Como YouTube usa HTTPS, inmediatamente después se realiza el handshake TLS/SSL: cliente y servidor intercambian certificados y claves para cifrar toda la comunicación posterior.

5. El cliente envía la solicitud HTTP/HTTPS:

Sobre esa conexión segura, el navegador envía una petición HTTP (método GET) pidiendo el recurso, por ejemplo la página principal de YouTube o el video específico. Esta petición incluye cabeceras con información como el tipo de navegador, cookies de sesión, idioma preferido, etc.

6. El servidor procesa la solicitud:

El servidor de YouTube recibe la petición, la procesa (autentica al usuario si aplica, consulta bases de datos, localiza el archivo de video en sus sistemas de almacenamiento/CDN) y prepara una respuesta HTTP con código de estado (200 OK si todo sale bien), más el contenido: HTML, CSS, JavaScript y los fragmentos del video en streaming.

7. El navegador renderiza y reproduce:

El cliente recibe la respuesta y empieza a interpretar el HTML/CSS/JS para construir la página, mientras el reproductor de video comienza a descargar y reproducir el contenido en fragmentos (streaming adaptativo), ajustando la calidad según el ancho de banda disponible, hasta que el video aparece en pantalla.

## 2. Frontend y Backend en acción

Frontend (lo que ve y usa el paciente/médico):

Es toda la interfaz con la que el usuario interactúa: el formulario para elegir fecha y hora de la cita, el calendario visual, los botones de confirmar/cancelar, las notificaciones en pantalla, etc. Se ejecuta en el navegador o app del dispositivo del usuario.

Tres tecnologías posibles:

-React (o Vue/Angular) — para construir la interfaz de usuario de forma dinámica y por componentes.
-HTML/CSS — estructura y estilo visual de las páginas (calendario, formularios).
-JavaScript/TypeScript — lógica en el cliente: validar que la fecha elegida sea válida, mostrar mensajes de error, actualizar la pantalla sin recargar.

Backend (lo que ocurre "detrás de cámaras"):

Es la lógica del servidor: verificar disponibilidad del médico, guardar la cita en la base de datos, evitar que dos pacientes reserven el mismo horario, enviar confirmaciones por correo, manejar la autenticación de usuarios, etc.

Tres tecnologías posibles:

-Node.js (Express) o Python (Django/FastAPI) — para crear la lógica del servidor y las rutas de la API.
-PostgreSQL o MySQL — base de datos para almacenar pacientes, médicos, horarios y citas.
-Java (Spring Boot) — alternativa robusta para sistemas más grandes, típico en entornos de salud con requisitos estrictos.

Cómo se comunican frontend y backend:
El frontend nunca accede directamente a la base de datos; en su lugar, hace una petición (request) HTTP a una API (Interfaz de Programación de Aplicaciones) que expone el backend. Por ejemplo, cuando el paciente hace clic en "Agendar cita", el frontend envía algo como:
POST /api/citas con los datos (paciente, médico, fecha, hora) en el cuerpo de la petición.
Esta petición viaja por el protocolo HTTP/HTTPS, especificando el método (GET para consultar horarios disponibles, POST para crear una cita, PUT/PATCH para modificarla, DELETE para cancelarla).
El backend recibe la request, ejecuta la lógica necesaria (revisa disponibilidad, guarda en la base de datos) y devuelve una respuesta (response): normalmente en formato JSON, con un código de estado como 201 Created (cita creada con éxito) o 409 Conflict (el horario ya está ocupado).
El frontend recibe esa respuesta y actualiza la pantalla en consecuencia: muestra un mensaje de "¡Cita confirmada!" o un error si algo falló.

En esencia, la API es el "contrato" que define qué peticiones puede hacer el frontend y qué respuestas dará el backend, y el ciclo request → proceso en servidor → response se repite cada vez que el usuario interactúa con la app.

## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|-------------|------------------------|------------------------|-------------------------------|-----------------------------------|
| REST        | JSON (comúnmente), también XML | Media — el servidor define qué devuelve cada endpoint | Baja | Alta |
| SOAP        | XML (estricto, con esquema WSDL) | Baja — protocolo rígido y estandarizado | Alta | Baja |
| GraphQL     | JSON | Alta — el cliente decide qué datos pedir | Media | Media |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**

GraphQL suele ser la opción más conveniente para un sistema de reservas en línea, ya que permite al frontend pedir exactamente los datos que necesita en cada consulta, reduciendo peticiones y peso de las respuestas. REST también es una alternativa sólida por su simplicidad y rapidez de implementación. SOAP no es recomendable aquí por su rigidez y complejidad, más apta para sistemas empresariales antiguos con requisitos estrictos de seguridad.

## 4. Explorando APIs con Postman

### 4.1 Selección de la API

-

**
Nombre de la API: PokéAPI

**
-

**
Descripción: PokéAPI es una API RESTful pública y gratuita que ofrece información completa sobre el universo de Pokémon: datos de cada Pokémon (estadísticas, tipos, habilidades, movimientos, evoluciones), items, ubicaciones, generaciones de juegos, cadenas evolutivas, entre otros. No requiere autenticación ni token, lo que la hace ideal para practicar consultas HTTP y explorar el formato JSON de respuesta. Todas las peticiones son de tipo GET, y se accede mediante endpoints como:

https://pokeapi.co/api/v2/pokemon/pikachu

que devuelve toda la información disponible sobre ese Pokémon en formato JSON.

**

### 4.2 Configuración en Postman

- **Nombre de la colección:** PokeAPI

- **Solicitudes agregadas:**

  - **GET** - "Obtener Pokemon": consulta el endpoint `{{base_url}}/pokemon/pikachu` (donde `base_url` = `https://pokeapi.co/api/v2`) y devuelve toda la información del Pokémon Pikachu (estadísticas, tipos, habilidades, etc.) en formato JSON, con respuesta `200 OK`.

  - **POST** - "Crear recurso": envía una solicitud a `https://reqres.in/api/users` con un body en formato JSON (`{"name": "Ash", "job": "Entrenador Pokemon"}`) para simular la creación de un nuevo recurso. Incluye el header `x-api-key` con la API key gratuita obtenida en ReqRes. Devuelve `201 Created` junto con el recurso creado y su nuevo id.

  - **PUT** - "Actualizar recurso": envía una solicitud a `https://reqres.in/api/users/2` con un body en formato JSON actualizado, para simular la modificación de un recurso existente. También incluye el header `x-api-key`. Devuelve `200 OK` con los datos actualizados.

- **Variables de entorno (Environment "PokeAPI Env"):**
  - `base_url` → `https://pokeapi.co/api/v2` (usada en la solicitud GET)
  - `api_key` → la API key gratuita de ReqRes (usada en los headers de POST y PUT)

### 4.3 Ejecución y análisis

| Solicitud | Método | Endpoint | Código de estado | Notas |
|-----------|--------|----------|-------------------|-------|
| Obtener Pokemon | GET | `{{base_url}}/pokemon/pikachu` | 200 OK | Se obtuvo correctamente toda la información de Pikachu (estadísticas, tipos, habilidades) en formato JSON. No requiere autenticación. |
| Crear recurso | POST | `https://reqres.in/api/users` | 201 Created | Se envió un body JSON con los datos de un nuevo usuario. ReqRes simuló la creación y devolvió el recurso con un id nuevo. Requirió el header `x-api-key` para evitar el error 429 (Too Many Requests) del plan gratuito. |
| Actualizar recurso | PUT | `https://reqres.in/api/users/2` | 200 OK | Se envió un body JSON con datos actualizados. El servidor respondió confirmando la actualización del recurso, también usando el header `x-api-key`. |

### 4.4 Explicación técnica

Cada solicitud sigue el ciclo **request → proceso en servidor → response**, propio del protocolo HTTP:

- **GET** se utiliza para *consultar* información sin modificar nada en el servidor. Es un método "seguro" e idempotente: ejecutarlo varias veces no cambia el estado de los datos. En este caso, el cliente (Postman) pidió los datos del Pokémon Pikachu y el servidor de PokéAPI respondió con el recurso solicitado.

- **POST** se utiliza para *crear* un nuevo recurso en el servidor. A diferencia de GET, no es idempotente: cada vez que se ejecuta, en teoría se crea un recurso nuevo (por eso ReqRes devolvió un `id` distinto). El código `201 Created` confirma explícitamente que el recurso fue creado con éxito, a diferencia del `200 OK` genérico.

- **PUT** se utiliza para *actualizar* un recurso existente, reemplazando sus datos. Es idempotente: ejecutarlo varias veces con el mismo body produce el mismo resultado final. El código `200 OK` indica que la actualización se procesó correctamente.

- El **header `x-api-key`** fue necesario para las solicitudes a ReqRes porque esta API, en su plan gratuito, limita la cantidad de peticiones por minuto sin autenticación (lo que generó inicialmente el error `429 Too Many Requests`). Al incluir la key en los headers, el servidor identifica al cliente y le permite mayor cuota de uso.

- Las **variables de entorno** (`base_url`, `api_key`) evitan repetir datos fijos en cada solicitud y facilitan cambiar de entorno (por ejemplo, de pruebas a producción) sin reescribir URLs o credenciales manualmente.

En conjunto, este ejercicio demuestra el ciclo completo de comunicación entre cliente y servidor mediante una API REST: el cliente arma una solicitud con un método HTTP específico, el servidor la procesa según su lógica interna, y responde con un código de estado que indica el resultado de la operación.

####

### 4.4 Explicación técnica

#### Obtener Pokemon
- **Método HTTP:** GET
- **Endpoint:** `{{base_url}}/pokemon/pikachu`
- **Parámetros / body:** No requiere body. No necesita autenticación.
- **Descripción de la respuesta:** Devuelve un JSON con toda la información de Pikachu: id, nombre, altura, peso, tipos, habilidades, movimientos y estadísticas base. Código de estado `200 OK`.

#### Crear recurso
- **Método HTTP:** POST
- **Endpoint:** `https://reqres.in/api/users`
- **Parámetros / body:** Header `x-api-key` con la API key de ReqRes. Body JSON: `{"name": "Ash", "job": "Entrenador Pokemon"}`
- **Descripción de la respuesta:** El servidor simula la creación de un nuevo usuario y devuelve el objeto enviado junto con un `id` generado automáticamente y una marca de tiempo `createdAt`. Código de estado `201 Created`.

#### Actualizar recurso
- **Método HTTP:** PUT
- **Endpoint:** `https://reqres.in/api/users/2`
- **Parámetros / body:** Header `x-api-key` con la API key de ReqRes. Body JSON: `{"name": "Ash", "job": "Maestro Pokemon"}`
- **Descripción de la respuesta:** El servidor confirma la actualización devolviendo los datos enviados junto con una marca de tiempo `updatedAt`. Código de estado `200 OK`.

**¿Qué aprendiste del proceso?**

Aprendí a diferenciar en la práctica los métodos HTTP más comunes (GET, POST, PUT) y cómo cada uno tiene un propósito y un comportamiento distinto (idempotencia, códigos de estado esperados). También entendí la importancia de los headers de autenticación (`x-api-key`) para controlar el acceso y los límites de uso de una API, y cómo las variables de entorno en Postman ayudan a mantener las solicitudes organizadas y reutilizables sin hardcodear URLs o credenciales.

### 4.5 Reflexión final

Este ejercicio me ayudó a entender que una API no es más que un conjunto de reglas y endpoints que permiten que dos sistemas se comuniquen de forma estructurada, sin que el cliente necesite saber cómo funciona internamente el servidor. Aprendí que cada método HTTP (GET, POST, PUT, DELETE) tiene un propósito claro y un comportamiento esperado (como la idempotencia), y que los códigos de estado (200, 201, 404, 429, etc.) son el lenguaje que usa el servidor para comunicar el resultado de cada operación, ya sea éxito, error o algún problema como un límite de peticiones excedido.

Postman fue clave para hacer tangible algo que normalmente ocurre "detrás de cámaras" en una aplicación web: pude armar manualmente cada solicitud (eligiendo método, URL, headers y body) y ver en tiempo real la respuesta exacta que devolvía el servidor, incluyendo su código de estado y el JSON recibido. Esto me permitió visualizar con claridad el ciclo completo de **request → procesamiento en el servidor → response**, y entender por qué el frontend de una aplicación real nunca accede directamente a una base de datos, sino que siempre pasa por una API que valida, procesa y responde a cada petición.