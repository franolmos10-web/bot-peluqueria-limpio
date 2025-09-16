from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)

# === CONFIGURACIÓN (rellena con tus claves) ===
# Solo si quieres usar OpenAI (opcional)
USE_OPENAI = False  # Cambia a True si tienes API key de OpenAI
openai.api_key = 'TU_API_KEY_OPENAI'  # Solo si USE_OPENAI = True

# === FUNCIÓN DE RESPUESTA DE LA IA ===
def responder_ia(mensaje_usuario):
    mensaje_usuario = mensaje_usuario.lower()

    if USE_OPENAI:
        # GPT-3 (OpenAI) responde
        respuesta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Un cliente escribe: {mensaje_usuario}\nBot contesta:",
            max_tokens=100,
            temperature=0.7
        )
        return respuesta.choices[0].text.strip()

    else:
        # IA simple con lógica personalizada
        if 'hola' in mensaje_usuario or 'buenas' in mensaje_usuario:
            return "¡Hola! ¿En qué puedo ayudarte hoy? 😊"
        elif 'horario' in mensaje_usuario:
            return "Estamos abiertos de lunes a sábado de 9:00 a 19:00."
        elif 'precio' in mensaje_usuario or 'cuánto' in mensaje_usuario:
            return "Nuestros precios: corte de cabello 20€, peinado 15€, tinte desde 30€."
        elif 'cita' in mensaje_usuario or 'reservar' in mensaje_usuario:
            return "Puedes reservar tu cita respondiendo con el día y hora que prefieras."
        else:
            return "Lo siento, no entendí tu mensaje 🤖. ¿Podrías reformularlo?"

# === RUTA DEL WEBHOOK DE TWILIO ===
@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    mensaje = request.values.get('Body', '')
    respuesta = responder_ia(mensaje)

    twilio_resp = MessagingResponse()
    twilio_resp.message(respuesta)

    return str(twilio_resp)

# === INICIAR EL SERVIDOR LOCAL ===
if __name__ == '__main__':
    print("Bot corriendo en http://localhost:5000")
    app.run(port=5000)
