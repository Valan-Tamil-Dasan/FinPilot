from typing import TypedDict


class ChatIn(TypedDict):
    """
    Schema for Chat Request
    """
    user_query : str


class ChatOut(TypedDict):
    """
    Schema for Chat Response
    """
    final_answer : str
