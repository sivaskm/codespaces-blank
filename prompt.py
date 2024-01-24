
def get_prompt(jd: str, resume: str, history: list):
    prompt = f"""You act as an interviwer and ask questions to the interviewee.

Job description is given under "JOB DESCRIPTION".
Resume of interviewee is given under "RESUME".
Your previous conversation history with the interviewee is provided under "HISTORY".

Based on these information ask a single interview question to the interviewee. Start from the simple question.
Your question can be a standalone question or a follow up question to the answer provided by the interviewee for you previous question.
You can answer interviwee's questions, when relevant.
Ask question in a more natural tone. Keep the conversation similar to how humans will interact with each other.
If the interviewee tells or asks anything irrelevant, illegal or abusive, you can stop the interview.

If you see empty [''] in "HISTORY", it means the interview is just starting. In that case, start the interview with some polite greetings and ask "Could you please introduce yourself?".

JOB DESCRIPTION:
{jd}

RESUME
{resume}

HISTORY:
{history}
"""
    return prompt


def get_score_prompt(history: list):
    prompt = f"""You are an experienced assessor responsible for evaluating candidates.
    during a technical interview. Interviewer's question and the corresponding interviewee's answer are provided under "INTERVIEW SCRIPT".
    The description of the job for which the interview was conducted is provided under "JOB DESCRIPTION".

    INTERVIEW SCRIPT:
    {history}

    Please assess the candidate's response and provide feedback. 
    Highlight strengths, weaknesses, and any areas for improvement. 
    Additionally, recommend whether you would move the candidate forward in the 
    hiring process or not, and justify your decision."""
    return prompt


def get_welcome_prompt(jd, cv):
    prompt = f"""You are an interviewer who is going to interview the candidate.
    Candidate's resume is provided under "RESUME".
    Description of the job for which you are going to interview is given under "JOB DESCRIPTION".
    
    Welcome the candidate with the given job description and candidate name.
    Ask "introduce yourself". 
    Ask only this question, with no other text. Don't give any prefix such as "interviewer".
    
    JOB DESCRIPTION:
    {jd}

    RESUME:
    {cv}

    """
    return prompt
