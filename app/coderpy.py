from transformers import TFGPTJForCausalLM, AutoTokenizer
import subprocess
import time
from dotenv import load_dotenv
import os


def get_code_suggestion(prompt):
    # Load the model and tokenizer 
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
    model = TFGPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="tf")

    # Generate code
    outputs = model.generate(inputs.input_ids, max_length=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def type_out_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def main():
    load_dotenv('../Coderpy/api-key.env')  # Load environment variables from .env file
    openai_api_key = os.getenv('OPENAI_API_KEY')

    if openai_api_key is None:
        print("API key not found. Please check your .env file.")
        return

    # Open Notepad++
    subprocess.Popen(["notepad++.exe"])
    time.sleep(5)  # Wait for Notepad++ to open

    # Capture user input and generate code suggestion
    prompt = 'code snipet'
    code_suggestion = get_code_suggestion(prompt)

    # Simulate typing the generated code into Notepad++
    type_out_text(code_suggestion)

if __name__ == "__main__":
    main()
    


