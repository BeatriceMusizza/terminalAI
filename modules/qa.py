from ai_client import ask

def run(question: str, profession: str = "general") -> str:
    if profession.lower() != "general":
        prompt = f"Answer the following question as if you are a {profession}:\n{question}"
    else:
        prompt = question
    return ask(prompt)
