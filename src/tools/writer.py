from langchain_core.tools import tool
from sqlalchemy.dialects.postgresql import insert
from src.db.deps import get_db
from src.models.financial_facts import FinancialFacts

# @tool
def insert_financial_metric(company : str, period : str, metric : str, value : float):
    """
    Insert or update a single numeric income statement metric for a company and period.

    Use only for final, structured financial numbers that must be stored in the database.
    Do NOT use for text, ranges, estimates, or explanations.

    Args:
        company (str): Company identifier or name.
        period (str): Financial period (e.g., "FY2023", "Q1-2024").
        metric (str): Normalized income statement metric name.
        value (float): Final numeric value.

    Returns:
        dict: {"status": "ok"} if successful, otherwise {"status": "error", ...}.
    """

    db = next(get_db())
    
    try:
        stmt = insert(FinancialFacts).values(
            company=company,
            period=period,
            metric=metric.lower(),
            value=value
        ).on_conflict_do_update(
            index_elements=["company", "period", "metric"],
            set_={"value": value}
        )

        db.execute(stmt)
        db.commit()

        return {"status" : "ok"}
    except Exception as e:
        db.rollback()
        return {
            "status": "error", "type": type(e).__name__,
            "message": str(e),
            "company": company,
            "period": period,
            "metric": metric
        }

# @tool
def batch_insert_financial_metrics(rows: list[dict]):
    """
    Insert or update multiple income statement metrics in bulk.

    Use only for structured, final numeric income statement records.
    Do NOT use for text, estimates, partial data, or unnormalized metrics.

    Args:
        rows (list[dict]): Each item must contain:
            - company (str)
            - period (str)
            - metric (str)
            - value (float)

    Returns:
        dict: {"status": "ok"} if all rows were written successfully, otherwise {"status": "error", ...}.
    """
    db = next(get_db())

    try:
        normalized_rows = []
        for r in rows:
            normalized_rows.append({
                "company": r["company"],
                "period": r["period"],
                "metric": r["metric"].lower(),
                "value": r.get("value"),
            })

        stmt = insert(FinancialFacts).values(normalized_rows)

        stmt = stmt.on_conflict_do_update(
            index_elements=["company", "period", "metric"],
            set_={"value": stmt.excluded.value}
        )

        db.execute(stmt)
        db.commit()

        return {"status": "ok", "rows": len(normalized_rows)}

    except Exception as e:
        db.rollback()
        return {"status": "error", "message": str(e)}

WRITER_TOOLS = [insert_financial_metric, batch_insert_financial_metrics]
# print(insert_financial_metric.invoke({"company" : "dsfa" , "period" : "ew", "metric" : "w3" , "value" : 67}))
# print(batch_insert_financial_metrics.invoke({"rows" : [{"company" : "dsfa" , "period" : "3ew", "metric" : "w3" , "value" : 67}, {"company" : "dsfa" , "period" : "ew", "metric" : "5ngi" , "value" : 63}]}))
