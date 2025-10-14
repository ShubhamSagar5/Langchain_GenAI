from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 

load_dotenv() 

model = ChatOpenAI(model='gpt-4',temperature=0.2,max_completion_tokens=10) 

res = model.invoke("What is capital of india") 

print(res)