
#  For get methord
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello worlddddddddd"}
# @app.get("/greet/{name}")
# async def greet(name: str) -> dict:



from fastapi import FastAPI, Body,status

app = FastAPI()

@app.post("/greet",status_code=status.HTTP_201_CREATED)
async def greet_post():
    return {"message": "Hello!"}