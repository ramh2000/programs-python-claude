import os
from anthropic import Anthropic

# 1. Inicializa el cliente (busca tu API key automáticamente en el sistema)
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# 2. Tu lista de tareas repetitivas (ejemplo: textos que quieres clasificar)
textos_a_procesar = [
    "El producto llegó roto y tarde. Exijo un reembolso.",
    "Me encantó el servicio, el envío fue super rápido.",
    "¿Tienen stock del modelo en color azul?"
]

# 3. El bucle (Loop) que automatiza el trabajo
for texto in textos_a_procesar:
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,  # 0 es ideal para tareas repetitivas porque la respuesta es consistente
        system="Clasifica el departamento: Soporte, Ventas o Felicitaciones. Responde solo con una palabra.",
        messages=[
            {"role": "user", "content": texto}
        ]
    )
    # 4. Imprime o guarda el resultado automático
    print(f"Texto: '{texto}' -> Departamento: {response.content[0].text}")
