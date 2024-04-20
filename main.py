from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    post: str
    published: bool = True
    rating : Optional[int] = None


my_posts = [
    {
    "id": 1,
    "title": "First post",
    "post": "This is the first post",
},
    {
    "id": 2,
    "title": "2nd post",
    "post": "This is the 2nd post",
},
]


@app.get("/")
async def root():
    return {"message": "Hellow World "}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts")
def createPost(post:Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0 , 1000000000000)
    my_posts.append(post_dict)
    return {"data":post_dict}
