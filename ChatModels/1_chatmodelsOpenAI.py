from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

#max_completion_tokens - defines how many tokens in output.
#temperature; low value emans looking for facts, and high value means asking for creating or out of box answers.
model =ChatOpenAI(model="gpt4", temperature=1, max_completion_tokens=25)

result =model.invoke("What is capital of Latvia?")

print(result.content)
