from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage, content

SQL_AGENT_PROMPT = """
You are a financial SQL reasoning agent.

You have access ONLY to the provided tools and ONLY to the metrics listed below.
You are NOT allowed to answer from memory.
You MUST call tools to obtain all financial facts.

COMPANY NAME RULE:
- Company identifiers in all tool calls MUST be in snake_case and lowercase.
- Example: "Reliance Industries" → reliance_industries
- Never use spaces, capitals, or special characters in company names.

STRICT RULES:
- Use ONLY the metrics explicitly listed in the registry.
- Never invent metric names or columns.
- If the user asks for something outside these metrics → respond that it is not available.
- If multiple metrics are required, plan tool calls step by step.
- Never guess values.
- When finished, return a clear final natural language answer.

If metric represents an expense (COGS, SG&A, OPEX),
present the magnitude as positive for readability.
"""

def render_metric_context(metric_registry: dict) -> str:
    lines = ["Available SQL Metrics:\n"]

    for name, meta in metric_registry.items():
        lines.append(
            f"- {name}\n"
            f"  • statement: {meta['statement']}\n"
            f"  • description: {meta['description']}\n"
        )

    return "\n".join(lines)

def build_sql_agent_messages(user_query: str, metric_registry : dict) -> list[AnyMessage]:
    metric_context = render_metric_context(metric_registry)
    content = f"""
        {SQL_AGENT_PROMPT}

        {metric_context}
        """
    return [
        SystemMessage(content=content),
        HumanMessage(content=user_query)
    ]
