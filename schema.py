from pydantic import BaseModel

class UserRequest(BaseModel):
    cv_id: str
    jd_id: str
    conv_id: str
    interviewer_input: str
    user_input: str