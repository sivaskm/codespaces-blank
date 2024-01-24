from prompt import get_prompt, get_score_prompt, get_welcome_prompt
from llm import get_resp_from_llm
from pypdf import PdfReader
from io import BytesIO
from db import DB
from schema import ScoreRequest, StartRequest
import uuid

db = DB("interview.db")

def get_score(score_request: ScoreRequest):
    conv_id = score_request.conv_id
    conversation = db.get_conversation(conv_id)
    prompt = get_score_prompt(conversation)
    resp = get_resp_from_llm(prompt)
    return resp


def start_interview(start_request: StartRequest):
    cv_id = start_request.cv_id
    jd_id = start_request.jd_id
    conv_id = str(uuid.uuid4())
    cv = db.get_cv(cv_id)
    jd = db.get_jd(jd_id)
    prompt = get_welcome_prompt(jd=jd, cv=cv)
    resp = get_resp_from_llm(prompt)
    return {
        "conv_id": conv_id,
        "interviewer_input": resp
    }



def save_conversation(conv_id: str, interviewer: str, interviewee: str):
    if interviewee != "" and interviewee != "":
        content = {
            "interviewer_input": interviewer,
            "interviewee_input": interviewee
        }
        msg_id = str(uuid.uuid4())
        db.set_msg(conv_id=conv_id, msg_id=msg_id, content=str(content))

def get_response(request):
    jd_id = request.jd_id
    cv_id = request.cv_id
    conv_id = request.conv_id
    save_conversation(conv_id=conv_id, interviewer=request.interviewer_input, interviewee=request.interviewee_input)
    data = db.get_data(jd_id, cv_id, conv_id)
    prompt = get_prompt(resume=(data.get(cv_id)), jd=(data.get(jd_id)), history=data.get(conv_id))
    print(prompt)
    resp = get_resp_from_llm(prompt)
    return resp

def extract_text_from_pdf(file):
    file_content = file.read()
    pdf_reader = PdfReader(BytesIO(file_content))
    return pdf_reader.pages[0].extract_text()

def save_text(text: str, file_name: str):
    with open(f"data/{file_name}.txt", "w") as text_file:
        text_file.write(text)

def save_jd(text, file):
    if file:
        text = extract_text_from_pdf(file.file)
    jd_id = str(uuid.uuid4())
    db.set_jd(jd_id, text)
    return {
        "jd_id": jd_id
    }

def save_cv(text, file):
    if file:
        text = extract_text_from_pdf(file.file)
    cv_id = str(uuid.uuid4())
    db.set_cv(cv_id, text)
    return {
        "cv_id": cv_id,
    }
