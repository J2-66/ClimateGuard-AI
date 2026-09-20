import os
import sys
from dotenv import load_dotenv

print("=" * 60)
print("        CLIMATEGUARD AI - SYSTEM HEALTH TEST")
print("=" * 60)

# ---------------------------------------------------------
# TEST 1: Python
# ---------------------------------------------------------

print("\n[1/8] Checking Python...")

print("Python version:", sys.version.split()[0])

if sys.version_info >= (3, 10):
    print("✅ Python version is suitable")
else:
    print("⚠️ Python 3.10+ is recommended")


# ---------------------------------------------------------
# TEST 2: Environment Variables
# ---------------------------------------------------------

print("\n[2/8] Checking environment variables...")

load_dotenv()

API_KEY = os.getenv("WATSONX_APIKEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
URL = os.getenv("WATSONX_URL")
MODEL_ID = os.getenv("WATSONX_MODEL_ID")

print("API Key:", "✅ Found" if API_KEY else "❌ Missing")
print("Project ID:", "✅ Found" if PROJECT_ID else "❌ Missing")
print("URL:", URL if URL else "❌ Missing")
print("Model:", MODEL_ID if MODEL_ID else "❌ Missing")

if not all([API_KEY, PROJECT_ID, URL, MODEL_ID]):
    print("\n❌ Environment configuration is incomplete.")
    sys.exit(1)


# ---------------------------------------------------------
# TEST 3: IBM watsonx SDK
# ---------------------------------------------------------

print("\n[3/8] Checking IBM watsonx SDK...")

try:
    from ibm_watsonx_ai import Credentials
    from ibm_watsonx_ai.foundation_models import ModelInference

    print("ibm_watsonx_ai: ✅ Installed")

except ImportError as e:
    print("ibm_watsonx_ai: ❌ Not installed")
    print("Error:", e)
    sys.exit(1)


# ---------------------------------------------------------
# TEST 4: Create Credentials
# ---------------------------------------------------------

print("\n[4/8] Creating IBM credentials...")

try:
    credentials = Credentials(
        url=URL,
        api_key=API_KEY
    )

    print("IBM credentials: ✅ Created")

except Exception as e:
    print("IBM credentials: ❌ Failed")
    print("Error:", e)
    sys.exit(1)


# ---------------------------------------------------------
# TEST 5: Connect to Granite
# ---------------------------------------------------------

print("\n[5/8] Connecting to IBM Granite...")

try:

    model = ModelInference(
        model_id=MODEL_ID,
        credentials=credentials,
        project_id=PROJECT_ID
    )

    print("Granite model connection: ✅ Successful")

except Exception as e:
    print("Granite model connection: ❌ Failed")
    print("Error:", e)
    sys.exit(1)


# ---------------------------------------------------------
# TEST 6: Simple Generation
# ---------------------------------------------------------

print("\n[6/8] Testing text generation...")

try:

    prompt = """
Explain climate change in simple English.
Give exactly 3 short sentences.
"""

    response = model.generate_text(
        prompt=prompt,
        params={
            "max_new_tokens": 100,
            "temperature": 0.2
        }
    )

    print("Granite generation: ✅ Successful")
    print("\nGranite response:")
    print("-" * 50)
    print(response)
    print("-" * 50)

except Exception as e:
    print("Granite generation: ❌ Failed")
    print("Error:", e)
    sys.exit(1)


# ---------------------------------------------------------
# TEST 7: ClimateGuard AI Structured Test
# ---------------------------------------------------------

print("\n[7/8] Testing ClimateGuard AI structured response...")

try:

    prompt = """
You are ClimateGuard AI.

Analyze this situation:

A city receives very heavy rainfall for several hours.
The river level is rising and some low-lying areas have
already experienced waterlogging.

Return your answer in this exact format:

Risk Level: <Low/Moderate/High/Critical>
Main Risk: <one short sentence>
Immediate Action: <one short sentence>
Safety Advice: <one short sentence>
"""

    response = model.generate_text(
        prompt=prompt,
        params={
            "max_new_tokens": 150,
            "temperature": 0.2
        }
    )

    print("ClimateGuard structured test: ✅ Successful")

    print("\nResponse:")
    print("-" * 50)
    print(response)
    print("-" * 50)

except Exception as e:
    print("ClimateGuard structured test: ❌ Failed")
    print("Error:", e)
    sys.exit(1)


# ---------------------------------------------------------
# TEST 8: Carbon Footprint Test
# ---------------------------------------------------------

print("\n[8/8] Testing carbon-footprint assistant...")

try:

    prompt = """
You are a climate awareness assistant.

A person uses 150 kWh of electricity per month
and travels 500 km per month by petrol car.

Explain briefly:
1. Which activities contribute to emissions.
2. Two practical ways to reduce emissions.

Use simple English.
"""

    response = model.generate_text(
        prompt=prompt,
        params={
            "max_new_tokens": 150,
            "temperature": 0.2
        }
    )

    print("Carbon assistant test: ✅ Successful")

    print("\nResponse:")
    print("-" * 50)
    print(response)
    print("-" * 50)

except Exception as e:
    print("Carbon assistant test: ❌ Failed")
    print("Error:", e)
    sys.exit(1)


# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("        🎉 CLIMATEGUARD AI SYSTEM TEST COMPLETE")
print("=" * 60)

print("""
✅ Python environment
✅ Environment variables
✅ IBM watsonx SDK
✅ IBM credentials
✅ WML project connection
✅ Granite model
✅ Text generation
✅ Flood-risk style response
✅ Carbon-footprint assistant

Your IBM Granite backend is ready for the next development phase.
""")