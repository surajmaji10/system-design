"""
@author: Akash Maji
@email: akashmaji@iisc.ac.in
"""

# import the class from library
from fastapi import FastAPI
from pydantic import BaseModel

# creating the main component of our app
app = FastAPI()

class CustomReqBody(BaseModel):
    age: int
    name: str

# my endpoint
@app.get("/ping")
async def ping():
    return {
        "message": "Hello",
        "from": "Akash Maji"
    }

# for home
@app.get("/")
async def hello():
    return "Hello Welcome."

# this will be NOW be read
@app.get("/blogs/comments")
async def blog_comment():
    return "No comments yet"

# with path params
@app.get("/blogs/{blog_id}")
async def blog(blog_id: int):
    # assert blog_id > 0
    content = "Hello " * blog_id
    return {"blog id": blog_id, \
            "content": content}

# # this wont be read
# @app.get("/blogs/comments")
# async def blog_comment():
#     return "No comments yet"

# query parameter
@app.get("/user")
async def users(id: int = None, name: str = None):
    return {"id": id, "name": name}

# request body (just use one reqbody (anywhere in the list))
@app.post("/users/{id}")
async def create(id: int, name: str = "", age: int = 0, \
                 reqbody: CustomReqBody = None):
    print(reqbody.name, reqbody.age)
    print("Creating user")
    return reqbody





