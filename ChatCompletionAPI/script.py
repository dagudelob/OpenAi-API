""" Clase para el uso de Assistants (Beta)
En esta clase hemos creado un asistente, y luego accedido a él para enviarle un mensaje a través de un hilo.
Después hemos ejecutado el asistente y hemos obtenido los pasos que ha realizado para responder a nuestro mensaje (incluyendo el uso de la herramienta Code Interpreter).
Finalmente, hemos obtenido la respuesta del asistente y hemos imprimido los pasos que ha realizado para responder a nuestro mensaje.  """

import os #variables de entorno 
from dotenv import load_dotenv #cargar variables de entorno
from openai import OpenAI #objeto de la API 
import requests
import json
import time

load_dotenv() #cargar variables de entorno

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # API key como atributo de la clase OpenAI

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", 
         "content": "te llamas Vision, presentate como asistente de IA"
         },
        {"role": "user",
         "content": "Hola, ¿cómo estás?"},
    ],
    max_tokens=100, # cantidad de tokens para la respuesta.
    temperature=0.2 # temperatura para la respuesta 0.9 es más creativo y 0.2 es más preciso
)

print(response.choices[0].message.content)

    