from pypdf import PdfReader
from typing import Union, Dict
from pathlib import Path
import requests
import logging

DIR = "data"


def init_dir(dir_path: Union[str, Path]) -> Path:
    if type(dir_path) is str:
        dir_path = Path(dir_path)
    if not dir_path.exists():
        dir_path.mkdir(parents=True)
    return dir_path


def _download_pdf(pdf_url: str, DIR: Union[str, Path] = DIR) -> Path:
    """
    Get the text from a PDF and parse it
    :param pdf_url:
    :param DIR
    :return:
    """
    logging.info(f"Downloading {pdf_url} text")
    pdf_filename = pdf_url.split("/")[-1]

    # Set up download
    DIR = init_dir(DIR)
    out_path = Path(DIR) / pdf_filename

    # Does file exist already
    if out_path.exists():
        return out_path

    # Get PDF file
    else:
        response = requests.get(pdf_url)
        with out_path.open("wb") as f:
            f.write(response.content)

    return out_path


def _parse_pdf(pdf_path: Union[Path, str]) -> str:
    """
    Read contents of a PDF files
    :param pdf_path:
    :return:
    """
    logging.info(f"Parsing text from {pdf_path}")
    if type(pdf_path) == str:
        pdf_path = Path(pdf_path)
    pdf_reader = PdfReader(pdf_path)

    # Initialize a string to store the text content
    pdf_text = ""
    n_pages = len(pdf_reader.pages)

    # Iterate through the pages and extract the text
    for page_num in range(n_pages):
        page = pdf_reader.pages[page_num]
        pdf_text += "\n" + page.extract_text()
    return pdf_text


def download_and_parse_pdf(pdf_url: str) -> str:
    """
    Get the text from a PDF and parse it
    :param pdf_url:
    :return:
    """
    logging.info(f"Downloading and reading text from {pdf_url}")
    pdf_path = _download_pdf(pdf_url)
    pdf_text = _parse_pdf(pdf_path)
    return pdf_text
