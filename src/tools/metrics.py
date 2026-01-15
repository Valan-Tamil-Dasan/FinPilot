from langchain_core.tools import tool

METRIC_REGISTRY = {

  "sales": {
    "statement": "income_statement",
    "description": "Total revenue from sale of goods and services before costs."
  },
  "cogs": {
    "statement": "income_statement",
    "description": "Cost of goods sold."
  },
  "operating_expenses": {
    "statement": "income_statement",
    "description": "All selling, general, administrative and R&D expenses."
  },
  "operating_profit": {
    "statement": "income_statement",
    "description": "Profit from operations before interest and tax (EBIT)."
  },
  "depreciation_amortization": {
    "statement": "income_statement",
    "description": "Non-cash depreciation and amortization expense."
  },
  "interest_expense": {
    "statement": "income_statement",
    "description": "Interest paid on borrowings."
  },
  "tax_expense": {
    "statement": "income_statement",
    "description": "Income tax expense."
  },
  "net_profit": {
    "statement": "income_statement",
    "description": "Profit attributable to shareholders after tax and interest."
  },


  "cash": {
    "statement": "balance_sheet",
    "description": "Cash and cash equivalents."
  },
  "short_term_investments": {
    "statement": "balance_sheet",
    "description": "Highly liquid short-term investments."
  },
  "current_assets": {
    "statement": "balance_sheet",
    "description": "Total current assets."
  },
  "non_current_assets": {
    "statement": "balance_sheet",
    "description": "Total non-current assets."
  },
  "total_assets": {
    "statement": "balance_sheet",
    "description": "Sum of all assets."
  },
  "current_liabilities": {
    "statement": "balance_sheet",
    "description": "Obligations due within one year."
  },
  "non_current_liabilities": {
    "statement": "balance_sheet",
    "description": "Long-term obligations."
  },
  "total_liabilities": {
    "statement": "balance_sheet",
    "description": "Sum of all liabilities."
  },
  "financial_debt": {
    "statement": "balance_sheet",
    "description": "Interest-bearing short and long-term borrowings."
  },
  "equity": {
    "statement": "balance_sheet",
    "description": "Shareholders’ equity."
  },
  "retained_earnings": {
    "statement": "balance_sheet",
    "description": "Accumulated retained earnings."
  },


  "operating_cash_flow": {
    "statement": "cashflow",
    "description": "Cash generated from operating activities."
  },
  "capex": {
    "statement": "cashflow",
    "description": "Capital expenditure on fixed assets."
  },
  "free_cash_flow": {
    "statement": "cashflow",
    "description": "Operating cash flow minus capital expenditure."
  },
  "investing_cash_flow": {
    "statement": "cashflow",
    "description": "Net cash from investing activities."
  },
  "financing_cash_flow": {
    "statement": "cashflow",
    "description": "Net cash from financing activities."
  },
  "dividends_paid": {
    "statement": "cashflow",
    "description": "Cash dividends paid to shareholders."
  },
}

METRIC_KEYS = [
  "sales",
  "cogs",
  "operating_expenses",
  "operating_profit",
  "depreciation_amortization",
  "interest_expense",
  "tax_expense",
  "net_profit",
  "cash",
  "short_term_investments",
  "current_assets",
  "non_current_assets",
  "total_assets",
  "current_liabilities",
  "non_current_liabilities",
  "total_liabilities",
  "financial_debt",
  "equity",
  "retained_earnings",
  "operating_cash_flow",
  "capex",
  "free_cash_flow",
  "investing_cash_flow",
  "financing_cash_flow",
  "dividends_paid",
]

@tool
def get_metric_registry() -> dict:
    """
    Return the dictionary of allowed Cannonical financial metrics
    """
    return METRIC_REGISTRY

METRIC_TOOLS = [get_metric_registry]
