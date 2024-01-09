# Dry run:
import os
from dotenv import load_dotenv
from openai import OpenAI
import logging

from utils.logger.loggerconfig import setup_logger
from utils.file_downloader.url_loader import download_and_parse_pdf
from utils.file_parser.chunker import chunk_text

# from agent.generic_agent import GenericAgent

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_APIKEY")

setup_logger()
logging.info("Starting program")

# pdf_url = "https://arxiv.org/pdf/2106.01345.pdf"
# pdf_path = download_and_parse_pdf(pdf_url)
# text = chunk_text(pdf_path)


if __name__ == "__main__":
    text = download_and_parse_pdf("https://arxiv.org/pdf/2106.01345.pdf")  # Success

    print(chunk_text(text)[0])  # Success
