from decimal import Decimal
from sqlalchemy import select
from langchain_core.tools import tool
from src.models.financial_facts import FinancialFacts 
from src.db.deps import get_db

@tool
def get_financial_metric(company: str, period: str, metric: str):
    """
    Retrieve a single income statement metric value for a company and period.

    Use only for structured financial queries.
    Do NOT use for explanations, summaries, or free-text questions.

    Args:
        company (str): Company identifier or name.
        period (str): Financial period (e.g., "FY2023", "Q1-2024").
        metric (str): Normalized income statement metric name.

    Returns:
        dict: {"company": str, "period": str, "metric": str, "value": float} if found, otherwise {"status": "not_found"}.
    """
    db = next(get_db())
    row = db.execute(
        select(FinancialFacts.value)
        .where(
            FinancialFacts.company == company,
            FinancialFacts.period == period,
            FinancialFacts.metric == metric.lower(),
        )
    ).scalar_one_or_none()

    if row is None:
        return {"value": None}

    if isinstance(row, Decimal):
        return {"value": float(row)}

    return {"value": row}

@tool
def get_financial_metrics_for_period(company: str, period: str):
    """
    Retrieve all financial metrics for a company in a given period.

    Args:
        company (str): Company identifier or name.
        period (str): Financial period (e.g., "FY2023", "Q1-2024").

    Returns:
        dict: {
            "company": str,
            "period": str,
            "metrics": {metric_name: float}
        }
        If no records are found, returns:
        {"company": str, "period": str, "metrics": {}}
    """
    db = next(get_db())

    rows = db.execute(
        select(FinancialFacts.metric, FinancialFacts.value)
        .where(
            FinancialFacts.company == company,
            FinancialFacts.period == period,
        )
    ).all()

    metrics = {}

    for metric, value in rows:
        if isinstance(value, Decimal):
            value = float(value)
        metrics[metric] = value

    return {
        "company": company,
        "period": period,
        "metrics": metrics,
    }

@tool
def get_metric_trend(company: str, metric: str):
    """
    Retrieve the historical trend of a financial metric across all periods for a company.

    Args:
        company (str): Company identifier or name.
        metric (str): Normalized financial metric name.

    Returns:
        dict: {
            "company": str,
            "metric": str,
            "trend": [
                {"period": str, "value": float},
                ...
            ]
        }
    """
    db = next(get_db())

    rows = db.execute(
        select(FinancialFacts.period, FinancialFacts.value)
        .where(
            FinancialFacts.company == company,
            FinancialFacts.metric == metric.lower(),
        )
        .order_by(FinancialFacts.period)
    ).all()

    trend = []

    for period, value in rows:
        if isinstance(value, Decimal):
            value = float(value)
        trend.append({"period": period, "value": value})

    return {
        "company": company,
        "metric": metric,
        "trend": trend,
    }

ATOMIC_TOOLS = [get_metric_trend, get_financial_metrics_for_period, get_financial_metric]
