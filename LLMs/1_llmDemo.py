from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

llm= OpenAI(model='gpt3.5')

#prompt to be passed only
result = llm.invoke("What is the capital of India?")

print(result)

