from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 

load_dotenv() 


model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

chathistory = []

while True:
    userInput = input('You: ') 
    chathistory.append(userInput)
    if userInput == 'exit': 
        break
    result =  model.invoke(chathistory) 
    chathistory.append(result)
    print("AI: ",result.content) 

print(chathistory)