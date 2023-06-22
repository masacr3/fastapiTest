from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.medicacion_routes import medicacion

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
        )


app.include_router(medicacion)

#@app.get("/")
#async def root():
#    return {"mensaje" : "hello world"}

#@app.get("/marto")
#async def marto():
#    return { "mensaje" : "el codigo marto ha sido activado"}
