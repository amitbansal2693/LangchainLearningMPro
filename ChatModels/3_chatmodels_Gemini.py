from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5pro")

result =model.invoke("What is capital of Latvia?")

print(result.content)