from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate

prompt= PromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a poetic translator."),
    ("human", "Translate to Spanish: Roses are red, violets are blue."),
    ("ai", "Las rosas son rojas, las violetas azules."),
    ("human", "Translate to Spanish: The sun is bright."),
])

print(prompt)