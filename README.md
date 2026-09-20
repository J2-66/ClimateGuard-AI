# ClimateGuard AI

ClimateGuard AI is a student prototype for the 1M1B–IBM SkillsBuild AI for Sustainability internship.

## Features
- Climate awareness chatbot using local RAG
- Optional IBM Granite generation through watsonx.ai
- Carbon footprint estimation
- Transparent flood-risk decision support
- Text/PDF/DOCX/image input
- Entity/summary-oriented multimodal workflow
- Responsible-AI safeguards

## SDG alignment
Primary: SDG 13 – Climate Action.
Secondary: SDG 11 – Sustainable Cities and Communities.

## Architecture

User
  -> Streamlit UI
  -> Agent-style routing
      -> Climate question -> RAG -> Granite (optional)
      -> Carbon question -> Carbon calculator
      -> Flood question -> Risk model
      -> Document/image -> Extraction -> RAG/Granite summary

## Setup on Windows

```powershell
cd climateguard_ai
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## IBM Granite setup

1. Create/access a watsonx.ai project.
2. Create an IBM Cloud API key.
3. Copy the project ID.
4. Set environment variables:

```powershell
$env:WATSONX_APIKEY="YOUR_KEY"
$env:WATSONX_PROJECT_ID="YOUR_PROJECT_ID"
$env:WATSONX_URL="https://us-south.ml.cloud.ibm.com"
$env:WATSONX_MODEL_ID="ibm/granite-4.1-8b"
streamlit run app.py
```

Do not put API keys directly in source code or GitHub.

## RAG
Knowledge files are stored in `knowledge_base/`. The prototype retrieves relevant passages before generation. Replace the included educational files with authoritative sustainability documents for a stronger final demo.

## Important limitation
The carbon factors are illustrative. The flood module is an educational transparent risk-score prototype, not a real flood forecasting service. For a production system, use validated local environmental datasets and official authorities.

## Suggested demo questions
- What are practical ways to reduce household carbon emissions?
- Why does soil moisture affect flood risk?
- What should people do during heavy rainfall?
- Upload a sustainability PDF and summarize it.
