from pydantic import BaseModel

class Medicacion(BaseModel):
    nombre : str
    vto : str
    cantidad : str

