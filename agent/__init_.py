# Use different agent for different classes. Should be moduler, which means we should define it to be simple enough.
# Agent should do one thing: given a pdf, return a list of results/flags. The exact things to be ran by the agent should be moduler and changable.

# Dry run:
import os
from dotenv import load_dotenv
from openai import OpenAI
import logging

load_dotenv()
oai_client = OpenAI()
oai_client.api_key = os.getenv("OPENAI_APIKEY")
