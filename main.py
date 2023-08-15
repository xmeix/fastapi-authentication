import uvicorn
from fastapi import FastAPI
from app.model import PostSchema


posts = [
    {
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "content": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    },
    {
        "id": 2,
        "title": "qui est esse",
        "content": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
    },
    {
        "id": 3,
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "content": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
    },
    {
        "id": 4,
        "title": "eum et est occaecati",
        "content": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit",
    },
]

users = []

app = FastAPI()


# GET test
@app.get("/", tags=["test"])
def greet():
    return {"hello": "world"}


# GET Posts
@app.get("/posts", tags=["posts"])
def getPosts():
    return {"data": posts}


# Get single post {id}
@app.get("/posts/{id}", tags=["posts"])
def getPost(id: int):
    if id > len(posts):
        return {
            "error": 'post with ID: "{id}" does not exist',
        }

    for post in posts:
        if post["id"] == id:
            return {"data": post}


# post a post
@app.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.model_dump())
    return {"info": "Post added"}



