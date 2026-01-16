from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
def index():
    return {"data" : {"Name" : "wali"}}

@app.get('/about')
def about():
    return {"data" : "This is the about page"}