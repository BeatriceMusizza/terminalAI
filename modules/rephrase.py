from ai_client import ask

def run(text: str, style: str = "formal", tone: str = None, audience: str = None) -> str:
    prompt = f"Rephrase this in a {style} style"
    if tone:
        prompt += f", with a {tone} tone"
    if audience:
        prompt += f", for an audience of {audience}"
    prompt += f":\n{text}"
    return ask(prompt)
