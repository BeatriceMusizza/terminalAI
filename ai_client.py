import os
import requests

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN') or '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'}",  
    "Content-Type": "application/json"
}

def ask(prompt, max_tokens=300): #300 default
    system_prompt = "You are a helpful AI assistant."
    full_prompt = f"<|system|>\n{system_prompt}\n<|user|>\n{prompt}\n<|assistant|>"

    payload = {
        "inputs": full_prompt,
        "parameters": {
            "max_new_tokens": max_tokens,
            "do_sample": True,
            "temperature": 0.7
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload) #link to the API
    response.raise_for_status()
    output = response.json()[0]["generated_text"] 
    return output[len(full_prompt):]  # strip prompt from output
