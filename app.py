import logging
import os

import google.generativeai as palm
import streamlit as st
import yaml
from dotenv import load_dotenv


CONTEXT = """"
Explain the topic of "{}" in a short text format that is targeted at the general public. The tone of the text should be informative and easy to understand with some examples.
﻿"""

st.set_page_config(
    page_title="PaLM-based content creation",
    page_icon="🌴",
)


@st.cache_resource()
def parse_configs(configs_path: str):
    configs = yaml.safe_load(open(configs_path, "r"))
    logger.info(f"Configs: {configs}")
    return configs


@st.cache_resource()
def setup_keys():
    palm.configure(api_key=os.getenv("API_KEY"))


def query(prompt: str, defaults: dict):
    response = palm.generate_text(**defaults, prompt=prompt)
    return response


# API_KEY loaded from the `.env` file which is not visible for obvious reasons
CONFIGS_PATH = "configs.yaml"


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)

load_dotenv()
setup_keys()

configs = parse_configs(CONFIGS_PATH)

st.title("PaLM-based content creation")
input = st.text_input(label="Enter a topic to generate content")

prompt = CONTEXT.format(input)
logger.info(f"Prompt: {prompt}")

generate = st.button("Generate")

if generate:
    with st.spinner("Generating content..."):
        response = query(prompt, configs)

    tab1, tab2, tab3 = st.tabs(["Content #1", "Content #2", "Content #3"])

    with tab1:
        st.header("Generated content #1")
        st.write(response.candidates[0]["output"])

    with tab2:
        st.header("Generated content #2")
        st.write(response.candidates[1]["output"])

    with tab3:
        st.header("Generated content #3")
        st.write(response.candidates[2]["output"])
