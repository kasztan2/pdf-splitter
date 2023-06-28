from pdf_splitter.split import split_pdf_by_y_coordinates
from pdf_splitter.find import find_sep
from pdf2image import convert_from_path
import os

def split_pdf(filename: str, output_path: str, sep: str):
    os.makedirs(f"{output_path}/pdf", exist_ok=True)
    os.makedirs(f"{output_path}/img", exist_ok=True)

    splits = find_sep(filename, sep)
    splits.reverse()
    prev = 0
    i = -1

    for split in splits:
        i += 1
        y = split[0]
        page_num = split[1]
        name = split[2]
        if y == prev:
            continue

        if y == 0:
            prev = 0
            continue

        split_pdf_by_y_coordinates(
            filename, prev, y, f"{output_path}/pdf/{name}.pdf", page_num
        )
        convert_from_path(f"{output_path}/pdf/{name}.pdf", use_cropbox=True)[0].save(
            f"{output_path}/img/{name}.png", "PNG"
        )
        prev = y
