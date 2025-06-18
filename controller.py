from model.model import get_resume_feedback, get_interview_questions

def process_request(task: str, resume_text: str, role: str) -> str:
    """
    Routes the task to the appropriate model function.

    Parameters:
        task (str): either "feedback" or "interview"
        resume_text (str): raw extracted resume text
        role (str): job title the user is targeting

    Returns:
        str: LLM-generated output
    """
    if not resume_text or not role:
        return "Missing resume or role input."

    if task == "feedback":
        return get_resume_feedback(resume_text, role)
    elif task == "interview":
        return get_interview_questions(resume_text, role)
    else:
        return "Invalid task selected. Please choose 'feedback' or 'interview'."