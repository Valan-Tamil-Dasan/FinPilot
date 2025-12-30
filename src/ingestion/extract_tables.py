from typing_extensions import Doc
import pdfplumber
import pandas as pd


pdf_path = "assets/World_Bank_Group_Annual_Report_2025.pdf"
# pdf_path = "assets/2024-universal-registration-document_tcm564-510443.pdf"
pdf_path  = "assets/One_Page.pdf"

def extract_tables(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables():
                df = pd.DataFrame(table[1:], columns=table[0])
                tables.append(df)
    return tables

from unstructured.partition.pdf import partition_pdf
from unstructured.documents.elements import Table

def extract_tables_unstructured(pdf_path):
    elements = partition_pdf(pdf_path,strategy="hi_res")
    tables = []
    for el in elements:
        if isinstance(el, Table):
            html = el.metadata.text_as_html
            df = pd.read_html(html)[0]
            tables.append(df)
    return tables


# import pdfplumber
# from collections import defaultdict
# import pandas as pd
# import re


# def detect_columns(words):
#     xs = sorted([w["x0"] for w in words])
#     cols = [xs[0]]
#     for x in xs[1:]:
#         if x - cols[-1] > 40:   # finance column gap
#             cols.append(x)
#     return cols
#
# def cluster_rows(words):
#     rows = defaultdict(list)
#     for w in words:
#         y = round(w["top"] / 3) * 3
#         rows[y].append(w)
#     return rows
#
# def build_table(words, columns):
#     rows = cluster_rows(words)
#     table = []
#
#     for y in sorted(rows):
#         row = [""] * len(columns)
#         for w in rows[y]:
#             for i, cx in enumerate(columns):
#                 if abs(w["x0"] - cx) < 40:
#                     row[i] += " " + w["text"]
#         table.append([c.strip() for c in row])
#     return table
#
# with pdfplumber.open(pdf_path) as pdf:
#     page = pdf.pages[0]
#     words = page.extract_words(
#         use_text_flow=True,
#         x_tolerance=1,
#         y_tolerance=3
#     )
#
# columns = detect_columns(words)
# table = build_table(words, columns)
#
# import pandas as pd
# df = pd.DataFrame(table)
# print(df)


from docling.document_converter import DocumentConverter

converter = DocumentConverter()
doc = converter.convert(pdf_path)

tables = doc.document.tables
print(doc.document.export_to_markdown())



# def extract_text(pdf_path : str):
#     pages = []
#     with pdfplumber.open(pdf_path) as pdf:
#         pages = pdf.pages
#     return pages
#
# print(extract_text(pdf_path))
