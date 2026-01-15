
import re


def to_snake_case(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)   
    text = re.sub(r'_+', '_', text)           
    return text.strip('_')
