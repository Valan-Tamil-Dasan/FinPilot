from src.prompts.retrieval.query_translation import build_query_translation_messages
from src.runtime.llms import get_llm
from src.states.retrieval.user_query import TranslatedQuery, UserQuery


def query_translator(state : UserQuery) -> TranslatedQuery:
    """
    Node that is used to Translate Query
    """
    user_query = state["user_query"]

    llm = get_llm()

    response = llm.invoke(build_query_translation_messages(user_query))
     
    translated_query : TranslatedQuery = {
            "user_query" : user_query,
            "translated_query" : str(response.content)
    }

    return translated_query
