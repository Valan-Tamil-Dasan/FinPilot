from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition


load_dotenv()

# define llm
llm = init_chat_model(model="groq:openai/gpt-oss-120b")
# define tools

@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b

sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs. Make use of the tools available and give an accurate result")

def tool_calling_llm(state : MessagesState):
    return {"messages" : [llm_with_tools.invoke([sys_msg]+ state["messages"])]}

# bind tools
tools = [multiply, add, divide]
llm_with_tools = llm.bind_tools(tools)

# add nodes
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm" , tool_calling_llm)
builder.add_node("tools" , ToolNode(tools))


# add edges
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges("tool_calling_llm" , tools_condition)
builder.add_edge("tools" , "tool_calling_llm")

# compile

graph = builder.compile()
