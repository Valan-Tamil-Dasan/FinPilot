from src.tools.aggregation import AGGREGATION_TOOLS
from src.tools.atomic import ATOMIC_TOOLS

TOOLS = AGGREGATION_TOOLS + ATOMIC_TOOLS 
TOOL_MAP = {t.name: t for t in TOOLS}
