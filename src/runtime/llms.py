from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from functools import lru_cache
from src.tools.tools import TOOLS

load_dotenv()

@lru_cache
def get_llm():
    llm = init_chat_model(model="groq:openai/gpt-oss-120b")
    return llm

@lru_cache
def get_llm_with_tools():
    llm = get_llm()
    llm_with_tools = llm.bind_tools(TOOLS)
    return llm_with_tools
