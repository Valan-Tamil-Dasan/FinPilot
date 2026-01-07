from langchain_core.messages import HumanMessage, SystemMessage


TEXT_DISTILL_PROMPT = """
You are a financial narrative memory compiler.

Convert the given financial text into atomic financial meaning units.

Return ONLY valid JSON array.
Each item must follow exactly this schema:

{
  "text_type": "policy | risk | profit_driver | obligation | auditor_opinion | management_commentary | other",
  "text_summary": "<concise factual meaning>",
}

Rules:
- Extract explicit financial meaning only
- Do NOT summarize vaguely
- Do NOT invent facts
- Split into minimal atomic units
- Return JSON ONLY
"""

def build_text_distill_messages(text: str):
    return [
        SystemMessage(content=TEXT_DISTILL_PROMPT),
        HumanMessage(content=text)
    ]
