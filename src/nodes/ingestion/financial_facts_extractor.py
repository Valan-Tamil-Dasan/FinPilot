import re
from src.prompts.ingestion.financial_fact_extractor import build_financial_fact_extractor_messages
from src.states.ingestion.financial_facts_extractor import FinancialFact, FinancialFacts, TableBlocksWithCompany
from src.states.ingestion.table_distllizer import TableBlocks
from src.runtime.llms import get_llm
from src.tools.metrics import METRIC_TOOLS, get_metric_registry
from src.tools.writer import WRITER_TOOLS
import json

from src.utils.string_utils import to_snake_case



def financial_facts_extractor(state : TableBlocksWithCompany) -> FinancialFacts:
    """
    Extract Financial Facts 
    Financial Fact : 
        company : str
        period : str
        metric : str
        value : float
    """

    financial_facts : FinancialFacts = {
            "financial_facts" : []
    }
    
    llm = get_llm() 
    metrics = get_metric_registry.invoke({})
    company = to_snake_case(state.get("company",""))

    for block in state["table_blocks"]:
        table_md = block["content"]

        response = str(llm.invoke(build_financial_fact_extractor_messages(table_md,metrics)).content)

        try:
            facts = json.loads(response)
        except Exception as e:
            print("LLM is not returning a valid json")
            continue 

        for fact in facts:
            financial_fact : FinancialFact = {
                    "company" : company,
                    "metric" : fact.get("metric", ""),
                    "period" : fact.get("period" , ""),
                    "value" : fact.get("value", "")
            }
            financial_facts["financial_facts"].append(financial_fact)

    return financial_facts
