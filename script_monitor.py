import requests
import smtplib
import os

# Configuración de las credenciales del correo electrónico
EMAIL_ADDRESS = os.environ.get('EMAIL_USER') 
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def email_notification():
    """
    Función para enviar una notificación por correo electrónico si el servidor no responde.
    """
    try:
        # Establece la conexión con el servidor SMTP de Gmail
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()  # Inicia la comunicación con el servidor SMTP
            smtp.starttls()  # Habilita el cifrado TLS
            smtp.ehlo()  # Inicia la comunicación con el servidor SMTP nuevamente (después de habilitar TLS)
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Inicia sesión en la cuenta de correo

            # Configura el mensaje del correo
            subject = 'EL SERVIDOR NO RESPONDE'
            body = 'Asegúrate de que el servidor está en funcionamiento o reinícialo de ser necesario.'
            msg = f'Subject: {subject}\n\n{body}'  # Formatea el mensaje con asunto y cuerpo

            # Configura el remitente y el destinatario del correo
            SENDER = EMAIL_ADDRESS
            RECEIVER = '#'  # Reemplaza '#' con la dirección de correo del destinatario

            # Envía el correo electrónico
            smtp.sendmail(SENDER, RECEIVER, msg)

    except Exception as e:
        print(f"Error al enviar el correo: {e}")

try:
    # URL del endpoint a verificar
    url = '#'  # Reemplaza '#' con la URL del endpoint

    # Realiza la petición GET al endpoint con un tiempo de espera de 5 segundos
    r = requests.get(url, timeout=5)

    # Verifica el código de estado de la respuesta
    if r.status_code != 200:
        email_notification()  # Envía una notificación si el código de estado no es 200

except requests.exceptions.RequestException as e:
    # Maneja las excepciones de la librería requests (e.g., timeout, conexión rechazada)
    print(f"Error en la petición HTTP: {e}")
    email_notification()  # Envía una notificación si ocurre un error en la petición

except Exception as e:
    # Maneja cualquier otra excepción que pueda ocurrir
    print(f"Error inesperado: {e}")
    email_notification()  # Envía una notificación si ocurre un error inesperado
