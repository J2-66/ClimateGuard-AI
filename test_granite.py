import os
from dotenv import load_dotenv

from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference


# Load .env
load_dotenv()


# Read configuration
API_KEY = os.getenv("WATSONX_APIKEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
URL = os.getenv("WATSONX_URL")
MODEL_ID = os.getenv("WATSONX_MODEL_ID")


print("===================================")
print(" ClimateGuard AI - Granite Test")
print("===================================")

print("API Key:", "Found" if API_KEY else "Missing")
print("Project ID:", "Found" if PROJECT_ID else "Missing")
print("URL:", URL)
print("Model:", MODEL_ID)


# Check configuration
if not API_KEY:
    raise ValueError("WATSONX_APIKEY is missing")

if not PROJECT_ID:
    raise ValueError("WATSONX_PROJECT_ID is missing")

if not URL:
    raise ValueError("WATSONX_URL is missing")

if not MODEL_ID:
    raise ValueError("WATSONX_MODEL_ID is missing")


# Create IBM credentials
credentials = Credentials(
    url=URL,
    api_key=API_KEY
)


# Create Granite model
model = ModelInference(
    model_id=MODEL_ID,
    credentials=credentials,
    project_id=PROJECT_ID
)


# Send a test question
prompt = """
Explain climate change in simple English.
Give the answer in 3 short sentences.
"""


print("\nConnecting to IBM Granite...")
print("Please wait...\n")


try:

    response = model.generate_text(
        prompt=prompt
    )

    print("===================================")
    print(" SUCCESS! IBM GRANITE IS WORKING")
    print("===================================\n")

    print("Granite response:")
    print(response)

except Exception as e:

    print("===================================")
    print(" ERROR: GRANITE CONNECTION FAILED")
    print("===================================\n")

    print("Error:")
    print(e)