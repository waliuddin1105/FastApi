from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
def index():
    return {"data" : {"Name" : "wali"}}

@app.get('/blog/unpublished')
def unpublished():
    return {"data" : "Unpublished blogs"}

@app.get('/blog/{id}')
def getBlog(id : int):
    return {"data" : id}

@app.get('/blog/{id}/comments')
def comments(id : int):
    return {"data" :  {'1','2'}}
    
