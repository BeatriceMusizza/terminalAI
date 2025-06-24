from ai_client import ask

def run(command: str) -> str:
    prompt = f"Explain this terminal command like a man page:\n\n{command}"
    return ask(prompt)
