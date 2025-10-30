from langchain.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv 

load_dotenv()
 

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

text = "what is the capital of india" 

vector = embedding.embed_query(text)
print(vector)  # list of floats (embedding vector)
