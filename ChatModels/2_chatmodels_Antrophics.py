from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model_name="calude-3.5")

result =model.invoke("What is capital of Latvia?")

print(result.content)