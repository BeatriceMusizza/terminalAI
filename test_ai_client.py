from ai_client import ask

if __name__ == "__main__":
    prompt = "Explain the command `ls -alh` like a Linux man page." #what will be send
    response = ask(prompt)
    print("AI Response:\n", response)
