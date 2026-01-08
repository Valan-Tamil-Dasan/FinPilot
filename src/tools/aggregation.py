from decimal import Decimal
from sqlalchemy import select
from langchain_core.tools import tool
from src.models.financial_facts import FinancialFacts 
from src.db.deps import get_db

@tool
def sum_metric(company: str, metric: str, periods: list[str]):
    """
    Sum a financial metric over multiple periods.

    Args:
        company (str): Company identifier.
        metric (str): Metric name.
        periods (list[str]): List of periods to sum.

    Returns:
        {
          "company": str,
          "metric": str,
          "periods": list[str],
          "sum": float
        }
    """
    db = next(get_db())

    rows = db.execute(
        select(FinancialFacts.value)
        .where(
            FinancialFacts.company == company,
            FinancialFacts.metric == metric.lower(),
            FinancialFacts.period.in_(periods),
        )
    ).scalars().all()

    total = 0.0
    for v in rows:
        if isinstance(v, Decimal):
            v = float(v)
        total += v

    return {
        "company": company,
        "metric": metric,
        "periods": periods,
        "sum": total,
    }

@tool
def average_metric(company: str, metric: str, periods: list[str]):
    """
    Compute average value of a metric over multiple periods.

    Returns:
        {
          "company": str,
          "metric": str,
          "periods": list[str],
          "average": float
        }
    """
    db = next(get_db())

    rows = db.execute(
        select(FinancialFacts.value)
        .where(
            FinancialFacts.company == company,
            FinancialFacts.metric == metric.lower(),
            FinancialFacts.period.in_(periods),
        )
    ).scalars().all()

    values = []
    for v in rows:
        if isinstance(v, Decimal):
            v = float(v)
        values.append(v)

    avg = sum(values) / len(values) if values else None

    return {
        "company": company,
        "metric": metric,
        "periods": periods,
        "average": avg,
    }

AGGREGATION_TOOLS = [average_metric, sum_metric]
