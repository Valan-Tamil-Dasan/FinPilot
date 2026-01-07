from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage, content

QUERY_TRANSLATION_PROMPT = """
You are a financial search query translator.

Rewrite the user question into a short paragraph that will be used for semantic document retrieval.

Rules:
- Do NOT answer the question and do not define
- Preserve the full meaning of the question
- Expand abbreviations into full financial terms when helpful
- Include common synonyms of important financial concepts
- Keep time periods and company/entity names
- Do NOT include filler phrases like “tell me”, “what is”, etc.
- Output a single compact paragraph, not bullet points
"""

def build_query_translation_messages(user_query : str) -> list[AnyMessage]:
    """
    Funtion that Builds messages for the given user query
    """
    return [
        SystemMessage(content=QUERY_TRANSLATION_PROMPT),
        HumanMessage(content=user_query)
    ]
