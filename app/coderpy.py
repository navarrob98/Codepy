import openai
import os
import pyautogui
import time
import subprocess
import time
from dotenv import load_dotenv

def main():
    print('hello')
    load_dotenv()  # Load variables from .env file
    openai.api_key = os.getenv('OPENAI_API_KEY')
    # Launch VSCode
    subprocess.Popen(["notepad++"])
    time.sleep(5)  # Give VSCode time to open
    # Get the code suggestion
    prompt = input('')
    code_suggestion = get_code_suggestion(prompt)
    # Type the code into VSCode
    type_out_text(code_suggestion)
    print('bye')

def get_code_suggestion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5",
        messages=[
            {"role": "system", "content": "You are a helpful programming assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def type_out_text(text, delay=0.05):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)





