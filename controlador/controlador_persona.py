personas = []

def add_persona(persona):
    personas.append(persona)

def buscar_persona(rut):
    for persona in personas:
        if persona.getRut() == rut:
            return persona
    return None

def obtener_personas():
    return personas