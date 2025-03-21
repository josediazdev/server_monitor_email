# Monitor de Endpoints con Notificación por Correo Electrónico

Este programa en Python verifica la disponibilidad de un endpoint de servidor y envía una notificación por correo electrónico de Gmail si el servidor no responde con un código de estado 200 o si ocurre un error durante la petición.

Este programa es útil en los siguientes escenarios:

* **Monitoreo de disponibilidad de APIs**: Asegura que tus APIs críticas estén siempre en línea.
* **Monitoreo de servicios web**: Verifica que tus sitios web y aplicaciones web estén disponibles para los usuarios.
* **Alertas tempranas**: Recibe notificaciones inmediatas si un servicio falla, permitiéndote actuar rápidamente.
* **Automatización de tareas de mantenimiento**: Integra este script en tus sistemas de monitoreo para automatizar la detección de problemas.

## Requisitos

* Python 3.x
* Librerías: `requests`, `smtplib`, `os`

## Configuración

Antes de ejecutar el programa, debes configurar las siguientes variables de entorno:

* `EMAIL_USER`: Tu dirección de correo electrónico desde la cual se enviarán las notificaciones.
* `EMAIL_PASS`: La contraseña de tu correo electrónico.

Además, debes modificar las siguientes variables en el script:

* `url`: La URL del endpoint que deseas monitorear.
* `RECEIVER`: La dirección de correo electrónico del destinatario de las notificaciones.

## Uso

1.  Asegúrate de tener Python 3.x instalado.
2.  Instala las librerías necesarias:

    ```bash
    pip install requests
    ```

3.  Configura las variables de entorno `EMAIL_USER` y `EMAIL_PASS`.
4.  Modifica las variables `url` y `RECEIVER` en el script.
5.  Ejecuta el script:

    ```bash
    python3 script_monitor.py
    ```

## Ejemplo de variables de entorno

En sistemas Linux o macOS, puedes configurar las variables de entorno de la siguiente manera:

```bash
export EMAIL_USER="[dirección de correo electrónico eliminada]"
export EMAIL_PASS="tu_contraseña"
```


¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este programa, por favor abre un issue o envía un pull request.
