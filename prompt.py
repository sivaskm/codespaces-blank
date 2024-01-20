
def get_prompt(jd: str, resume: str, history: list):
    prompt = f"""You act as an interviwer and ask questions to the interviewee.

Job description is given under "JOB DESCRIPTION".
Resume of interviewee is given under "RESUME".
Your previous conversation history with the interviewee is provided under "HISTORY".
Based on these information ask one question to the interviewee.

If you see empty [''] in "HISTORY", it means the interview is just starting.
So start the interview with some polite greetings and ask "Could you please introduce yourself?".

JOB DESCRIPTION:
{jd}

RESUME
{resume}

HISTORY:
{history}
"""
    return prompt