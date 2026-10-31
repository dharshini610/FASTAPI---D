from fastapi import FastAPI 
app = FastAPI() 
@app.get("/") #decorator 
def read_root():
    return {"Dharsh's first API!"}

@app.get("/name")
def read_name():
    return {"message": "Andrum endrum SUPERSTAR! ⭐"}