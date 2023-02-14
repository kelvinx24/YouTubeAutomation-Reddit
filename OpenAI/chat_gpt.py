import openai
import config

model="text-davinci-003"

def ask_prompt(question, token_limit=1000):
     try:

        my_config = config.load_config()
        openai.api_key = my_config["OpenAi"]["api_key"]

        completion = openai.Completion.create(model=model, prompt=question, max_tokens=token_limit)
        return completion["choices"][0]["text"]

     except Exception as e:
        print(e)
        return ""