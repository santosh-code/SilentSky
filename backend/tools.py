from backend.llm_config import llm
from db.journal_db import get_today_logs
from backend.prompt_templates import reflection_prompt

def reflect_emotions(user_id):
    journal = get_today_logs(user_id)
    if not journal:
        return "No logs found for today."
    prompt = reflection_prompt.format(journal=journal)
    response = llm.invoke(prompt).content.strip()
    return response


def gita_verse_for_emotion(emotion):
    prompt = (
        f"Provide a Bhagavad Gita verse and interpretation to guide someone feeling '{emotion}'."
    )
    return llm.invoke(prompt).content.strip()