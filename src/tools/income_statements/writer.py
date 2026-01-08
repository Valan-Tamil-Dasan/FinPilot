from langchain_core.tools import tool
from sqlalchemy.dialects.postgresql import insert
from src.db.deps import get_db
from src.models import income_statement
from src.models.income_statement import IncomeStatement

def insert_income_metric(company : str, period : str, metric : str, value : float):
    """
    Insert or update a single statement metric
    """

    db = next(get_db())
    
    try:
        stmt = insert(IncomeStatement).values(
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
            "status": "error",
            "type": type(e).__name__,
            "message": str(e),
            "company": company,
            "period": period,
            "metric": metric
        }
