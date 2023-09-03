import logging
import os
from dotenv import load_dotenv
import google.generativeai as palm


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)
load_dotenv()

# API_KEY is loaded from the `.env` file which is not visible for obvious reasons
palm.configure(api_key=os.getenv("API_KEY"))

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [
      {"category":"HARM_CATEGORY_DEROGATORY","threshold":4},
      {"category":"HARM_CATEGORY_TOXICITY","threshold":4},
      {"category":"HARM_CATEGORY_VIOLENCE","threshold":4},
      {"category":"HARM_CATEGORY_SEXUAL","threshold":4},
      {"category":"HARM_CATEGORY_MEDICAL","threshold":4},
      {"category":"HARM_CATEGORY_DANGEROUS","threshold":4}
      ],
}

CONTEXT = """You are a content creation helper who helps to turn technical concepts into short text easier to understand.
Explain the following concept in a short text format, and give some examples: """

prompt = f"""{CONTEXT}Machine learning models usually overfit small datasets"""

logger.info(f"Prompt: {prompt}")

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
logger.info(f"Prompt: {response.result}")
