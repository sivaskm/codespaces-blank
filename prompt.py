
def get_prompt(jd: str, resume: str):
    prompt = f"""You are an expert in machine learning and you have 20 years of experience in this field.
Job description is given under "JOB DESCRIPTION".
Resume of interviewee is given under "RESUME".
Based on these information ask one question to the interviewee.

Ask a question to the interviewee.
Kindly analyse the job description, resume and chat history before asking any question.
"""
    return prompt