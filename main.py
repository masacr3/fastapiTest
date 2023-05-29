from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"mensaje" : "hello world"}

@app.get("/marto")
async def marto():
    return { "mensaje" : "el codigo marto ha sido activado"}
