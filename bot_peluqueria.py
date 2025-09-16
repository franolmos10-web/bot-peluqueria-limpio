from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()  # Cargar variables del archivo .env

# Ahora puedes acceder a las variables de entorno
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)



# Base de preguntas frecuentes y respuestas
faq = {
    "horario": "Nuestro horario es de lunes a sábado de 9am a 7pm.",
    "precio corte": "El corte de cabello cuesta $20.",
    "servicios": "Ofrecemos cortes, tintes, peinados y más.",
    "cita": "Puedes reservar tu cita llamando al 555-1234 o por WhatsApp.",
}

# Clasificación de clientes según mes (ejemplo)
clientes_por_mes = {
    "enero": [],
    "febrero": [],
    "marzo": [],
    # ...
}

def responder_pregunta(mensaje):
    mensaje = mensaje.lower()
    for clave in faq:
        if clave in mensaje:
            return faq[clave]
    return "Lo siento, no entendí tu pregunta. Por favor, pregúntame otra cosa."

def clasificar_cliente(nombre, mes):
    mes = mes.lower()
    if mes in clientes_por_mes:
        clientes_por_mes[mes].append(nombre)
        return f"Cliente {nombre} agregado al mes de {mes}."
    else:
        return "Mes no válido. Por favor, ingresa un mes válido."

# Ejemplo de uso:
if __name__ == "__main__":
    # Simula recibir un mensaje del cliente
    mensaje_cliente = "¿Cuál es el horario?"
    respuesta = responder_pregunta(mensaje_cliente)
    print("Bot responde:", respuesta)

    # Clasificar un cliente
    resultado = clasificar_cliente("Luis", "enero")
    print(resultado)

    # Enviar mensaje WhatsApp (asegúrate de cambiar los números)
    mensaje = client.messages.create(
        from_=from_whatsapp_number,
        to=to_whatsapp_number,
        body=respuesta
    )
    print(f"Mensaje enviado con SID: {mensaje.sid}")
