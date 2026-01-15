from langchain_core.messages import HumanMessage, SystemMessage, content

FINANCIAL_FACT_EXTRACTOR_PROMPT = """
You are a financial table extraction engine.

You are given:
• A markdown table from a company financial statement.
• A list of target canonical financial metrics.

Your task:
Extract values ONLY for the requested metrics.
Detect the periods from the table column headers.
Return one object per metric–period pair.

Rules:
- Map table row labels to the closest canonical metric.
- If a metric is not present, do not fabricate it.
- Convert numbers to floats.
- Remove commas and currency symbols.
- Use negative numbers if shown in parentheses.
- Return JSON only.
- No explanations.

Return format:
[
  {"metric": "<canonical_metric>", "period": "<period>", "value": <float>}
]
"""

def build_financial_fact_extractor_messages(table_md: str, metrics: dict):
    content = "These are the metrics : \n" +  str(metrics)  + "\n"
    content += "Table Summary : " + table_md

    return [
        SystemMessage(content=FINANCIAL_FACT_EXTRACTOR_PROMPT),
        HumanMessage(content=content)
    ]
