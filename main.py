from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/",status_code=201)
def read_root():
    return {"Hello": "World"}

class User(BaseModel):
    username: str="Niraj"
    email: str="niraj.221315@ncit.edu.np"

# POST endpoint
@app.post("/create-user/")
def create_user(user: User):
    return {
        "message": f"User {user.username} with email {user.email} created successfully!"
    }