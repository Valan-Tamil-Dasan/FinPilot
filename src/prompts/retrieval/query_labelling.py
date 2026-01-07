from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage, content

QUERY_LABELLING_PROMPT = """
Identify the intent of the user's query and classify it into exactly ONE of the allowed categories.

### CATEGORIES:
- policy: Rules, internal guidelines, or organizational procedures.
- risk: Potential liabilities, hazards, or mitigation strategies.
- financial_fact: Specific numerical data, balance sheet items, or historical performance.
- statement_line: Specific line items from a financial statement (e.g., Revenue, COGS).
- auditor_opinion: Statements regarding the fairness or accuracy of financial audits.
- profit_driver: Factors that directly impact the company's bottom line or growth.
- obligation: Legal or financial commitments and liabilities.
- management_commentary: Insights, outlooks, or narrative from company leadership.
- table_summary: Requests to summarize or explain a specific table or data grid.
- other: General inquiries that do not fit the above.

Note: If the user asks 'What is [Financial Term]?', it is a FINANCIAL_FACT because they are seeking a specific data point, not a definition.

### OUTPUT FORMAT:
Output ONLY the category name in lowercase. Do not provide explanations, preamble, or punctuation.
"""

def build_query_labelling_messages(user_query : str, translated_query : str) -> list[AnyMessage]:
    """
    Funtion that Labels the query
    """
    content = f"user_query : {user_query}"

    return [
        SystemMessage(content=QUERY_LABELLING_PROMPT),
        HumanMessage(content=content)
    ]
