from granite_service import ask_granite
from prompts import CLIMATE_CHAT_PROMPT


def climate_chat(question):

    prompt = CLIMATE_CHAT_PROMPT.format(
        question=question
    )

    response = ask_granite(
        prompt,
        max_new_tokens=300,
        temperature=0.3
    )

    return response