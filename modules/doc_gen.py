from ai_client import ask

def run(file_path: str, scope: str = "both") -> str:
    with open(file_path) as f:
        code = f.read()

    if scope == "functions":
        prompt = f"Add detailed inline comments to each function in this code:\n\n{code}"
    elif scope == "general":
        prompt = f"Write a high-level description of what this code does:\n\n{code}"
    else:  # both
        prompt = f"Write a high-level summary and add inline comments to each function:\n\n{code}"

    return ask(prompt, max_tokens=500)

