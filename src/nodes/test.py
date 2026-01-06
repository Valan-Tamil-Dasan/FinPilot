from langchain_core.messages import SystemMessage
from src.agent.state import State
from src.runtime.llms import get_llm_with_tools
from src.tools.test import TOOLS


sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs. Make use of the tools available and give an accurate result")

def tool_calling_llm(state : State):
    llm_with_tools = get_llm_with_tools()
    return {"messages" : [llm_with_tools.invoke([sys_msg]+ state["messages"])]}
