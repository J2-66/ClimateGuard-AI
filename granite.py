import os
import requests

def granite_chat(system_prompt, user_prompt):
    api_key = os.getenv("WATSONX_APIKEY")
    project_id = os.getenv("WATSONX_PROJECT_ID")
    url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
    model_id = os.getenv("WATSONX_MODEL_ID", "ibm/granite-4.1-8b")

    if not api_key or not project_id:
        return "IBM Granite is not configured. Set WATSONX_APIKEY and WATSONX_PROJECT_ID."

    token_resp = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data={
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            "apikey": api_key
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30
    )
    token_resp.raise_for_status()
    token = token_resp.json()["access_token"]

    endpoint = url.rstrip("/") + "/ml/v1/text/chat?version=2025-10-25"
    payload = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "project_id": project_id,
        "model_id": model_id,
        "max_completion_tokens": 700,
        "temperature": 0.2
    }
    r = requests.post(
        endpoint,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=payload,
        timeout=90
    )
    r.raise_for_status()
    data = r.json()
    try:
        return data["choices"][0]["message"]["content"]
    except Exception:
        return str(data)
