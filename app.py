import logging
import os

import google.generativeai as palm
import streamlit as st
import yaml
from dotenv import load_dotenv

st.set_page_config(
    page_title="PaLM-based content creation",
    page_icon="🌴",
)


@st.cache_resource()
def parse_configs(configs_path: str):
    configs = yaml.safe_load(open(configs_path, "r"))
    logger.info(f"Configs: {configs['defaults']}")
    logger.info(f"Context: {configs['context']}")
    return configs


@st.cache_resource()
def setup_keys():
    palm.configure(api_key=os.getenv("API_KEY"))


def query(prompt: str, defaults: dict):
    response = palm.generate_text(**defaults, prompt=prompt)
    return response.result


# API_KEY loaded from the `.env` file which is not visible for obvious reasons
CONFIGS_PATH = "configs.yaml"


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)

load_dotenv()
setup_keys()

configs = parse_configs(CONFIGS_PATH)

st.title("PaLM-based content creation")
input = st.text_input("Enter a topic to generate content")

prompt = f"{configs['context']} {input}"
logger.info(f"Prompt: {prompt}")

generate = st.button("Generate")

if generate:
    with st.spinner("Generating content..."):
        response = query(prompt, configs["defaults"])
    st.write(response)
