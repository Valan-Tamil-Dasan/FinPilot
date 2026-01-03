from typing import cast
from src.states.financial_profile import FinancialProfile, IngestState
from docling.document_converter import DocumentConverter
import os
import pdfplumber
from pypdf import PdfReader
from langdetect import detect

MAX_FILE_SIZE_MB = 20
MIN_PAGES = 1
MIN_CHAR_COUNT = 500
MAX_PAGES = 30

converter = DocumentConverter()

def financial_document_validator(state: IngestState) -> FinancialProfile:
    """
    Deterministic PDF Validation Node
    """
    pdf_path = state["pdf_path"]

    # Technical

    if not os.path.exists(pdf_path):
        return {"technical_ok": False, "reject_reason": "FILE_NOT_FOUND"}

    if not pdf_path.lower().endswith(".pdf"):
        return {"technical_ok": False, "reject_reason": "NOT_A_PDF"}

    if os.path.getsize(pdf_path) > MAX_FILE_SIZE_MB * 1024 * 1024:
        return {"technical_ok": False, "reject_reason": "FILE_TOO_LARGE"}

    try:
        reader = PdfReader(pdf_path)
        page_count = len(reader.pages)
    except Exception:
        return {"technical_ok": False, "reject_reason": "PDF_CORRUPTED"}

    if page_count < MIN_PAGES:
        return {"technical_ok": False, "reject_reason": "TOO_FEW_PAGES"}

    # Text Layer

    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages: 
                text = page.extract_text()
                if text:
                    full_text += text
    except Exception:
        return {"technical_ok": False, "reject_reason": "TEXT_EXTRACTION_FAILED"}

    if len(full_text.strip()) < MIN_CHAR_COUNT:
        return {"technical_ok": False, "reject_reason": "NO_EXTRACTABLE_TEXT"}

    # Language

    try:
        if detect(full_text) != "en":
            return {"technical_ok": False, "reject_reason": "NON_ENGLISH_DOCUMENT"}
    except Exception:
        return {"technical_ok": False, "reject_reason": "LANG_DETECTION_FAILED"}

    # Accepted

    return {"technical_ok": True}

# state = cast(IngestState,{"pdf_path" : "assets/World_Bank_Group_Annual_Report_2025.pdf"})
# print(financial_document_validator(state))
