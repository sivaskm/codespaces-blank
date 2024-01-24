from pydantic import BaseModel

class UserRequest(BaseModel):
    cv_id: str
    jd_id: str
    conv_id: str
    interviewer_input: str
    interviewee_input: str

class ScoreRequest(BaseModel):
    conv_id: str

class StartRequest(BaseModel):
    cv_id: str
    jd_id: str