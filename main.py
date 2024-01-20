from fastapi import FastAPI 
from schema import UserRequest
from handler import save_cv, save_jd, extract_text_from_pdf
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from typing import Dict

app = FastAPI()


@app.post("/question")
async def query(user_request: UserRequest):
    response = get_response(user_request.user_input)
    return response


@app.post("/uploadjd/")
async def upload_job_description(text: str = Form(None), file: UploadFile = File(None)):
    # print(extract_text_from_pdf(file))
    save_jd(text, file)

@app.post("/uploadcv/")
async def upload_job_description(file: UploadFile = File(None)):
    save_cv(file)


