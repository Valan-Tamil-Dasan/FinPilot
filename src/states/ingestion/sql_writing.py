from typing import TypedDict

class SqlIngestionState(TypedDict):
    """
    Financial Facts successfully injected
    """
    success : bool
