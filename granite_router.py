import json

from granite_service import ask_granite


# =========================================================
# GRANITE AGENT CLASSIFIER
# =========================================================

def classify_question(question):

    prompt = f"""
You are the routing system for ClimateGuard AI.

Your task is to identify which specialized agent
should handle the user's question.

Available agents:

1. flood_agent
   - Floods
   - Heavy rainfall
   - River levels
   - Waterlogging
   - Flood safety
   - Flood risk

2. carbon_agent
   - Carbon footprint
   - CO2 emissions
   - Electricity emissions
   - Transport emissions
   - Flights
   - Ways to reduce emissions

3. rag_agent
   - Questions that should be answered using
     ClimateGuard AI's reference documents
   - Climate knowledge
   - Climate mitigation
   - Climate adaptation
   - Flood safety information
   - Carbon-footprint information

4. climate_agent
   - General climate questions
   - Environmental awareness
   - General climate education

User question:
{question}

Return ONLY valid JSON.

Use exactly this format:

{{
    "agent": "flood_agent"
}}

OR

{{
    "agent": "carbon_agent"
}}

OR

{{
    "agent": "rag_agent"
}}

OR

{{
    "agent": "climate_agent"
}}
"""

    response = ask_granite(
        prompt,
        max_new_tokens=50,
        temperature=0
    )

    return response


# =========================================================
# EXTRACT AGENT
# =========================================================

def get_agent(question):

    response = classify_question(question)

    try:

        # Remove possible markdown formatting
        cleaned = response.strip()

        cleaned = cleaned.replace(
            "```json",
            ""
        )

        cleaned = cleaned.replace(
            "```",
            ""
        )

        cleaned = cleaned.strip()

        data = json.loads(cleaned)

        agent = data.get("agent")

        valid_agents = [
            "flood_agent",
            "carbon_agent",
            "rag_agent",
            "climate_agent"
        ]

        if agent in valid_agents:

            return agent

    except Exception:

        pass


    # Safe fallback
    return "climate_agent"