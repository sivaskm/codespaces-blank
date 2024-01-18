from prompt import get_prompt
from data import jd, resume
from llm import get_resp_from_llm

def get_response(user_input):
    prompt = get_prompt(jd, resume)
    resp = get_resp_from_llm(prompt)
    return resp