from typing import TypedDict

class UserQuery(TypedDict):
    """
    State that shows user query
    """
    user_query : str

class TranslatedQuery(TypedDict):
    """
    State the contains
    The translated and normalized query
    """
    user_query : str
    translated_query : str
