import os
from dotenv import load_dotenv

from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------

load_dotenv()

API_KEY = os.getenv("WATSONX_APIKEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
URL = os.getenv("WATSONX_URL")
MODEL_ID = os.getenv("WATSONX_MODEL_ID")


# ---------------------------------------------------------
# Validate configuration
# ---------------------------------------------------------

if not API_KEY:
    raise ValueError("WATSONX_APIKEY is missing from .env")

if not PROJECT_ID:
    raise ValueError("WATSONX_PROJECT_ID is missing from .env")

if not URL:
    raise ValueError("WATSONX_URL is missing from .env")

if not MODEL_ID:
    raise ValueError("WATSONX_MODEL_ID is missing from .env")


# ---------------------------------------------------------
# Create IBM credentials
# ---------------------------------------------------------

credentials = Credentials(
    url=URL,
    api_key=API_KEY
)


# ---------------------------------------------------------
# Create Granite model
# ---------------------------------------------------------

model = ModelInference(
    model_id=MODEL_ID,
    credentials=credentials,
    project_id=PROJECT_ID
)


# ---------------------------------------------------------
# Granite function
# ---------------------------------------------------------

def ask_granite(
    prompt,
    max_new_tokens=300,
    temperature=0.2
):
    """
    Send a prompt to IBM Granite and return the response.
    """

    try:

        response = model.generate_text(
            prompt=prompt,
            params={
                "max_new_tokens": max_new_tokens,
                "temperature": temperature
            }
        )

        return response

    except Exception as e:

        return f"Granite Error: {str(e)}"