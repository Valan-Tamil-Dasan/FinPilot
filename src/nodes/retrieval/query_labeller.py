from src.prompts.retrieval.query_labelling import build_query_labelling_messages
from src.runtime.llms import get_llm
from src.states.ingestion.text_distillizer import BLOCK_TYPES
from src.states.retrieval.user_query import FinancialType, TranslatedQuery

def query_labeller(state : TranslatedQuery) -> FinancialType:
    """
    Node that is used to Label Query
    """
    user_query = state["user_query"]
    translated_query = state["translated_query"]

    llm = get_llm()

    response = llm.invoke(build_query_labelling_messages(user_query,translated_query))

    label : FinancialType = {
        "financial_type" : str(response.content)
    }

    return label
