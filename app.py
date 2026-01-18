from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

# Single model instance (OpenRouter)
model = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1"
)

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)


prompt = ChatPromptTemplate.from_template("Write a song for given {topic} with 100 words")

add_routes(
    app,
    prompt|model,
    path = "/song"
)

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)