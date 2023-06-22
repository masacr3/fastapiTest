def medicacion_serializer(medicacion) -> dict:
    return {
            "id" : str(medicacion["_id"]),
            "nombre" : medicacion["nombre"],
            "vto" : medicacion["vto"],
            "cantidad" : medicacion["cantidad"]
            }

def medicaciones_serializer(medicaciones) -> list:
    return [ medicacion_serializer(medicacion) for medicacion in medicaciones ]

