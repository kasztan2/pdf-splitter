import PyPDF2


def split_pdf_by_y_coordinates(input_path, y1, y2, output_path, page_num):
    with open(input_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        page = reader.pages[page_num]
        width = page.cropbox.lower_right[0]
        page.cropbox.lower_right = (width, y2)
        page.cropbox.upper_left = (0, y1)
        writer.add_page(page)

        with open(output_path, "wb") as output_file:
            writer.write(output_file)
