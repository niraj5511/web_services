from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def respond_hello():
    return {"message": "Hello, world!"}

@app.post("/hello")
def post_respond_hello():
    return {"name":"Priya",
            "roll":33}
