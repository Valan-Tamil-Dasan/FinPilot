from langchain_core.messages import HumanMessage, SystemMessage, content

TABLE_DISTILL_PROMPT = """
You are a financial data distillation engine.

Convert the table into explicit factual financial statements.

Rules:
- Preserve all numbers, years, metrics, and currencies.
- Do NOT summarize vaguely.
- Do NOT infer or add any information.
- Output only factual statements.
"""

def build_table_distill_messages(table_md: str):
    return [
        SystemMessage(content=TABLE_DISTILL_PROMPT),
        HumanMessage(content=table_md)
    ]
