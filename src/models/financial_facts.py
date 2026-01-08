from sqlalchemy import Column, String, Numeric, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class FinancialFacts(Base):
    __tablename__ = "financial_facts"

    company = Column(String, nullable=False)
    period = Column(String, nullable=False)
    metric = Column(String, nullable=False)
    value = Column(Numeric, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("company", "period", "metric"),
    )
