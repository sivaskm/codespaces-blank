from fastapi import FastAPI 
from schema import UserRequest
from handler import get_response

app = FastAPI()


@app.post("/question")
async def query(user_request: UserRequest):
    response = get_response(user_request.user_input)
    return response