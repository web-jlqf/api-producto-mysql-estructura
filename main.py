# main.py
from fastapi import FastAPI
from routers.product_router import router as product_router

app = FastAPI(title="API REST  - Productos")

app.include_router(product_router)

# Si quieres algo de prueba:
@app.get("/")
def root():
    return {"message": "API de productos funcionando"}
