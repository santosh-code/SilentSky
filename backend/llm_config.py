import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=groq_key, model="llama3-8b-8192")