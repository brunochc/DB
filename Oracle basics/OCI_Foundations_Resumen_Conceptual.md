# OCI Foundations: La Ciudad en la Nube (Resumen Conceptual)

Imagina que Oracle Cloud Infrastructure (OCI) es una **Gran Ciudad** donde puedes construir lo que quieras. Aquí te explico las partes más importantes usando esa idea.

## 1. La Estructura de la Ciudad (Infraestructura Global)
*   **Regiones (Las Ciudades):** Son lugares físicos en el mundo (como Santiago, Londres, Tokio). Cada ciudad es independiente.
*   **Dominios de Disponibilidad (ADs - Los Barrios):** Dentro de una ciudad (Región), hay barrios separados (ADs). Si se corta la luz en un barrio, los otros siguen funcionando.
*   **Dominios de Fallo (FDs - Las Manzanas):** Dentro de un barrio, hay grupos de casas (FDs). Es mejor construir tus casas en diferentes manzanas para que si se cae un árbol en una, no aplaste todas tus casas.

## 2. Identidad y Permisos (IAM - Pasaportes y Llaves)
*   **Identidad (Quién eres):** Es como tu pasaporte o carnet. Dice quién eres (Usuario).
*   **Grupos (Tu Equipo):** Es más fácil dar llaves a un grupo (ej. "Jardineros") que a cada persona una por una.
*   **Políticas (Las Reglas):** Son instrucciones escritas que dicen "Los Jardineros pueden entrar al Jardín, pero no a la Cocina". Sin una política, nadie puede hacer nada (por defecto todo está cerrado).
*   **Compartimentos (Las Habitaciones):** Organizas tus cosas en cajas o habitaciones separadas (ej. "Caja de Juguetes", "Caja de Herramientas") para no mezclar y controlar quién toca qué.

## 3. Redes (Networking - Carreteras y Direcciones)
*   **VCN (Tu Terreno Privado):** Es tu propio pedazo de tierra cercado donde pones tus cosas. Nadie entra si tú no quieres.
*   **Subnets (Subdivisiones):** Divides tu terreno en zonas más pequeñas (ej. zona de juegos, zona de trabajo).
*   **Direcciones IP (Direcciones de Casa):** Para que el cartero sepa dónde entregar el paquete.
    *   *Pública:* Cualquiera desde fuera puede llegar (si les dejas).
    *   *Privada:* Solo para moverse dentro de tu terreno.
*   **Load Balancer (El Recepcionista):** Recibe a todos los visitantes en la entrada y les dice "tú ve a la ventanilla 1, tú a la 2" para que no se llene una sola fila.

## 4. Computación (Compute - Casas y Fábricas)
*   **Bare Metal (Casa Unifamiliar):** Alquilas la casa entera para ti solo. Nadie más vive ahí. Es muy potente.
*   **Virtual Machine (Departamento):** Vives en un edificio grande. Tienes tu propio departamento privado, pero compartes el edificio con otros vecinos. Es más barato y flexible.
*   **Contenedores/Kubernetes (Hotel Cápsula):** Espacios muy pequeños y eficientes donde solo llevas lo justo y necesario (tu aplicación).
*   **Functions (Pago por uso):** Como un taxi. Solo lo usas cuando necesitas ir a un sitio y pagas solo por el viaje. No tienes que comprar el auto.

## 5. Almacenamiento (Storage - Almacenes y Closets)
*   **Block Volume (Disco Duro):** Es como el disco duro de tu compu. Rápido y guarda tus programas y archivos de trabajo.
*   **Object Storage (Caja Infinita):** Una caja mágica donde puedes tirar millones de fotos, videos o documentos y nunca se llena. Ideal para cosas que no necesitas cambiar a cada rato.
*   **File Storage (Carpeta Compartida):** Una carpeta en la red que muchas computadoras pueden abrir y leer al mismo tiempo.
*   **Archive Storage (El Sótano):** Para guardar cosas viejas que casi nunca usas (como fotos de hace 10 años). Es muy barato, pero tardas un poco en sacarlas.

## 6. Base de Datos (Database - La Biblioteca)
*   **Base de Datos:** Es como una biblioteca muy ordenada donde guardas información importante (clientes, ventas) para encontrarla rápido.
*   **Autonomous Database (Bibliotecario Robot):** Es una base de datos que se arregla, se protege y se actualiza sola. Tú solo la usas, el robot hace el trabajo sucio.

## 7. Seguridad (Policía y Muros)
*   **Security Lists / NSG (Porteros):** Están en la puerta de tu casa y revisan quién entra y quién sale. "Tú sí, tú no".
*   **WAF (Escudo):** Protege tu casa de ataques de "hackers" malos que vienen de internet.
*   **Vault (Caja Fuerte):** Donde guardas las llaves maestras y contraseñas secretas.

## 8. Costos y Gobierno (Ayuntamiento)
*   **Precios:** En OCI pagas por lo que usas (como la luz o el agua).
*   **Budgets (Presupuesto):** Pones una alarma para que te avise si estás gastando más dinero del que querías.
*   **Cost Analysis (Factura detallada):** Te muestra en qué te gastaste el dinero (¿fue en "Casas" o en "Almacenes"?).
