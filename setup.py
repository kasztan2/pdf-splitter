import setuptools

with open("README.md", "r") as f:
    description = f.read()

setuptools.setup(
    name="pdf_splitter",
    version="0.0.1",
    author="Krzysztof Chorzempa",
    packages=["pdf_splitter"],
    description="A python library to split pdf vertically by a string",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/kasztan2/pdf-splitter",
    license="MIT",
    python_requires=">=3.8",
    install_requires=["pdfminer", "pdf2image", "PyPDF2"],
)
