from flood_risk import calculate_flood_risk
from carbon_calculator import calculate_carbon_footprint
from climate_chatbot import climate_chat
from rag_service import ask_rag
from granite_router import get_agent

# =========================================================
# AGENT KEYWORDS
# =========================================================

FLOOD_KEYWORDS = [
    "flood",
    "flooding",
    "rainfall",
    "heavy rain",
    "river level",
    "waterlogging",
    "waterlogged",
    "inundation",
    "flood risk"
]

CARBON_KEYWORDS = [
    "carbon footprint",
    "carbon",
    "co2",
    "emission",
    "emissions",
    "electricity",
    "transport",
    "vehicle",
    "car",
    "flight",
    "flights"
]


RAG_KEYWORDS = [
    "according to the documents",
    "according to the document",
    "knowledge base",
    "reference",
    "document",
    "documents",
    "climate mitigation",
    "climate adaptation"
]


# =========================================================
# ROUTER
# =========================================================

def route_query(question):

    question_lower = question.lower()

    # Flood Agent
    for keyword in FLOOD_KEYWORDS:

        if keyword in question_lower:

            return "flood_agent"


    # Carbon Agent
    for keyword in CARBON_KEYWORDS:

        if keyword in question_lower:

            return "carbon_agent"


    # RAG Agent
    for keyword in RAG_KEYWORDS:

        if keyword in question_lower:

            return "rag_agent"


    # Default
    return "climate_agent"


# =========================================================
# FLOOD AGENT
# =========================================================

def run_flood_agent(question):

    return climate_chat(
        f"""
The user is asking about flooding.

User question:
{question}

Provide useful flood-awareness information.

Do not claim to provide an official emergency warning.
Use simple English.
"""
    )


# =========================================================
# CARBON AGENT
# =========================================================

def run_carbon_agent(question):

    return climate_chat(
        f"""
The user is asking about carbon emissions or carbon footprint.

User question:
{question}

Explain the concept clearly and provide practical
ways to reduce environmental impact.

Use simple English.
"""
    )


# =========================================================
# RAG AGENT
# =========================================================

def run_rag_agent(question):

    result = ask_rag(question)

    return result


# =========================================================
# GENERAL CLIMATE AGENT
# =========================================================

def run_climate_agent(question):

    return climate_chat(question)


# =========================================================
# MAIN AGENT EXECUTOR
# =========================================================

def run_agent(question):

    agent = route_query(question)


    if agent == "flood_agent":

        response = run_flood_agent(question)


    elif agent == "carbon_agent":

        response = run_carbon_agent(question)


    elif agent == "rag_agent":

        result = run_rag_agent(question)

        # RAG returns answer + sources
        if isinstance(result, tuple):

            response = result[0]

        else:

            response = result


    else:

        response = run_climate_agent(question)


    return {
        "agent": agent,
        "response": response
    }

def run_granite_agent(question):

    agent = get_agent(question)


    if agent == "flood_agent":

        response = run_flood_agent(question)


    elif agent == "carbon_agent":

        response = run_carbon_agent(question)


    elif agent == "rag_agent":

        result = run_rag_agent(question)

        if isinstance(result, tuple):

            response = result[0]

        else:

            response = result


    else:

        response = run_climate_agent(question)


    return {
        "agent": agent,
        "response": response
    }