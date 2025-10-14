from langchain_anthropic  import ChatAnthropic 
from dotenv import load_dotenv 

load_dotenv() 

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

res = model.invoke("what is capital of india")

print(res.content)