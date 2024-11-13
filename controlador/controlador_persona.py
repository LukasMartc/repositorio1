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

def delete_persona(rut):
    persona = buscar_persona(rut)
    if persona is None:
        return False
    else:
        personas.remove(persona)
        return True
    