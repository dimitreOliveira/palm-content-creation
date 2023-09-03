import logging
import os

import google.generativeai as palm
import yaml
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)
load_dotenv()

# API_KEY loaded from the `.env` file which is not visible for obvious reasons
palm.configure(api_key=os.getenv("API_KEY"))
CONFIGS_PATH = "configs.yaml"

configs = yaml.safe_load(open(CONFIGS_PATH, "r"))
logger.info(f"Configs: {configs['defaults']}")
logger.info(f"Context: {configs['context']}")

prompt = (
    f"""{configs['context']} Machine learning models usually overfit small datasets"""
)
logger.info(f"Prompt: {prompt}")

response = palm.generate_text(**configs["defaults"], prompt=prompt)
logger.info(f"Prompt: {response.result}")
