from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from meta_ai_api import MetaAI

app = FastAPI()
llama_model = MetaAI()

origins = [
    "http://localhost:3000",
    "http://0.0.0.0:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

""" Query("Hello") -> result
{
  "response": {
    "message": "Hello again! How's your day going so far?\n",
    "sources": [],
    "media": []
  }
}
"""
@app.get("/llama/{query}") #fix this garbage
async def pass_query(query: str):
    return {"response": llama_model.prompt(query)}


    