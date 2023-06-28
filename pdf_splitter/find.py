from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from typing import Pattern
import re


def find_sep(filename: str, regex: str | Pattern):
    if isinstance(regex, str):
        regex = re.compile(regex)
    f = open(filename, "rb")
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(f)

    res = []

    i = 0
    for page in pages:
        res.append((0, i, f"str_{i}"))
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                if regex.search(text) is not None:
                    res.append((y, i, regex.search(text).group(0)))
        i += 1

    return res
