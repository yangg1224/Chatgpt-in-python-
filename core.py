
# %%
#pip install openai
# %%
import openai
import os
# main benefit is to make your app easily supported on various different envs
from dotenv import load_dotenv
# %%
load_dotenv()
openai.api_key = os.getenv('APIkey')
# %%
response = openai.Completion.create(
    engine = "text-davinci-003",    # select model
    prompt = input("write your question ？"),     
    max_tokens = 512,               # response tokens
    temperature = 1,                # diversity related
    top_p = 0.75,                   # diversity related
    n = 1,                          # num of response
)

completed_text = response["choices"][0]["text"]
print(completed_text)
