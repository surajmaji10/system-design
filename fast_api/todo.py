"""
@author: Akash Maji
@email: akashmaji@iisc.ac.in
"""

# import libs
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# create main app
app = FastAPI()

# in-mem store
todos = {}

class ToDo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool = False

class ToDoUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    done: bool = True


# "shows a message on home screen"
@app.get("/")
def home():
    return "Welcome to the HOME!"

# "gets a list of all todos"
@app.get("/todos")
async def get_todos():
    left = {}
    for id in todos:
        if todos[id] is not None:
            left[id] = todos[id]
    return left

# "gets a particular todo"
@app.get("/todos/{id}")
async def get_a_todo(id: int):
    if id in todos and todos[id] is not None:
        return todos[id]
    return {"error": "ToDo Item with id={} NOT found".format(id)}

# "create a new todo"
@app.post("/todos/{id}")
async def put_a_todo(id: int, req_body: ToDo):
    assert id == req_body.id
    if id in todos:
        return {"error": "ToDo Item with id={} exists".format(id)}
    todos[id] = req_body.model_dump() #prefer
    # todos[id] = req_body.dict() #deprecated
    return req_body

# "delete a todo if exists"
@app.delete("/todos/{id}")
async def delete_a_todo(id: int):
    if id in todos and todos[id] is not None:
        todos[id] = None
        return {"success": "ToDo Item with id={} removed".format(id)}
    return {"error": "ToDo Item with id={} NOT found".format(id)} 
    


## problematic
# @app.put("/todos/{id}")
# async def update_a_todo(id: int, req_body: ToDoUpdate):
#     assert id == req_body.id
#     if id not in todos or todos[id] is None:
#         return {"error": "ToDo Item with id={} NOT found".format(id)}
#     req_body = req_body.dict()
#     print(req_body)
#     todos[id]["done"] = req_body["done"]
#     if "title" in req_body:
#         todos[id]["title"] = req_body["title"]
#     if "description" in req_body:
#         todos[id]["description"] = req_body["description"]
#     return todos[id]

@app.put("/todos/{id}")  
async def update_a_todo(id: int, req_body: ToDoUpdate):  
    assert id == req_body.id  
    if id not in todos or todos[id] is None:  
        return {"error": "ToDo Item with id={} NOT found".format(id)}  
    # Convert the request body to a dictionary, excluding unset fields  
    req_body = req_body.dict(exclude_unset=True)  
    # Update the ToDo item with only the provided fields  
    todos[id].update(req_body)  
    return todos[id]
    

