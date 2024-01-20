from prompt import get_prompt
from data import jd, resume
from llm import get_resp_from_llm
from pypdf import PdfReader
from io import BytesIO

def get_response(user_input):
    prompt = get_prompt(jd, resume)
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
    save_text(text, "jd")

def save_cv(file):
    if file:
        text = extract_text_from_pdf(file.file)
        save_text(text, "cv")