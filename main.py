from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/home')
def index():
    return {"data" : {"Name" : "wali"}}

@app.get('/blog')
def blogs(limit : int = 10, published : bool = True, sort  : Optional[str] = None):
    if published:
        return {"data" : f"{limit} blogs that have been published"}
    else:
        return{"data" : "No published blogs available"}

@app.get('/blog/unpublished')
def unpublished():
    return {"data" : "Unpublished blogs"}

@app.get('/blog/{id}')
def getBlog(id : int):
    return {"data" : id}

@app.get('/blog/{id}/comments')
def comments(id : int):
    return {"data" :  {'1','2'}}
    
class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')
def CreateBlog(data : Blog):
    return {"Success" : f"Blog with title {data.title} created!"}
