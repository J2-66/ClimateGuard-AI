# 🌍 ClimateGuard AI

### AI-Powered Environment & Climate Awareness Platform

ClimateGuard AI is an AI-powered environmental and climate awareness platform that combines **Machine Learning, IBM Granite, Retrieval-Augmented Generation (RAG), Agentic AI, Computer Vision, and rule-based environmental calculations** into a single interactive application.

The platform provides users with tools for **flood-risk awareness, carbon-footprint estimation, climate-related question answering, document analysis, image-based environmental analysis, and climate knowledge retrieval**.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Problem Statement](#-problem-statement)
* [Objectives](#-objectives)
* [Key Features](#-key-features)
* [AI and ML Technologies](#-ai-and-ml-technologies)
* [System Architecture](#-system-architecture)
* [Application Modules](#-application-modules)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Environment Variables](#-environment-variables)
* [Running the Application](#-running-the-application)
* [Machine Learning Model](#-machine-learning-model)
* [RAG Pipeline](#-rag-pipeline)
* [Agentic AI Workflow](#-agentic-ai-workflow)
* [Document Analysis](#-document-analysis)
* [Image Analysis](#-image-analysis)
* [Carbon Footprint Calculation](#-carbon-footprint-calculation)
* [Safety and Limitations](#-safety-and-limitations)
* [Deployment](#-deployment)
* [Future Scope](#-future-scope)
* [SDG Alignment](#-sdg-alignment)
* [Conclusion](#-conclusion)
* [Author](#-author)

---

# 🌱 Overview

Climate change and environmental risks require accessible tools that can help people understand environmental conditions and make informed decisions.

ClimateGuard AI provides a centralized platform where users can interact with different AI-powered environmental services.

The application uses **IBM Granite through IBM watsonx.ai** for natural-language generation and combines it with specialized modules for machine learning, retrieval, document processing, computer vision, and environmental calculations.

### Main capabilities

* 🌊 Flood Risk Prediction
* 🌱 Carbon Footprint Estimation
* 💬 Climate Awareness Chatbot
* 📚 Climate Knowledge Retrieval using RAG
* 🤖 Agentic AI Query Routing
* 📄 Environmental Document Analysis
* 🖼️ Environmental Image Analysis
* 🧠 IBM Granite-powered explanations

---

# ❗ Problem Statement

Environmental information is often distributed across different sources and can be difficult for non-technical users to interpret.

People may also lack simple tools for understanding:

* potential flood-risk conditions,
* personal carbon emissions,
* climate-related concepts,
* environmental documents,
* and visual environmental information.

ClimateGuard AI addresses this problem by integrating multiple AI and ML capabilities into one user-friendly platform.

---

# 🎯 Objectives

The main objectives of ClimateGuard AI are:

1. Develop an interactive environmental AI assistant.
2. Provide educational flood-risk predictions using Machine Learning.
3. Estimate carbon emissions using user-provided activity information.
4. Provide climate-related question answering using IBM Granite.
5. Implement Retrieval-Augmented Generation for document-based answers.
6. Implement an agent-based workflow for routing user queries.
7. Analyze uploaded environmental documents.
8. Perform basic computer-vision analysis on environmental images.
9. Provide practical environmental awareness recommendations.
10. Demonstrate the integration of modern AI technologies into an environmental application.

---

# 🚀 Key Features

## 🌊 1. Flood Risk Assistant

The Flood Risk Assistant uses a Machine Learning model to estimate flood-risk levels based on environmental conditions such as:

* Rainfall
* River level
* Waterlogging
* Previous flooding
* Temperature
* Humidity

The application returns:

* predicted risk level,
* model probabilities,
* major contributing factors,
* explanation generated using IBM Granite,
* safety recommendations.

> **Important:** The prediction is intended for educational and awareness purposes and is not an official emergency warning system.

---

## 🌱 2. Carbon Footprint Calculator

The Carbon Footprint module estimates monthly emissions based on:

* Electricity consumption
* Car travel
* Public transportation
* Flights

The application calculates estimated CO₂ emissions and provides environmental awareness suggestions.

The calculation uses predefined emission factors and is intended as an educational estimation rather than an official carbon-accounting system.

---

## 💬 3. Climate Awareness Chatbot

Users can ask general questions about:

* climate change,
* global warming,
* environmental protection,
* sustainability,
* climate adaptation,
* climate mitigation,
* renewable energy,
* pollution,
* and environmental awareness.

IBM Granite generates natural-language responses through IBM watsonx.ai.

---

## 📚 4. Retrieval-Augmented Generation (RAG)

ClimateGuard AI includes a RAG pipeline for answering questions using a local climate knowledge base.

The RAG system:

1. Loads climate-related documents.
2. Extracts document text.
3. Splits documents into smaller chunks.
4. Generates vector embeddings.
5. Compares the user query with document chunks.
6. Retrieves the most relevant information.
7. Sends the retrieved context to IBM Granite.
8. Generates a grounded response.

Supported document formats include:

* `.txt`
* `.pdf`

---

## 🤖 5. Agentic AI

ClimateGuard AI contains an agent-based query-routing workflow.

Depending on the user's question, the system can route the request toward specialized agents such as:

```text
User Query
     │
     ▼
Query Router
     │
     ├── Flood Agent
     │
     ├── Carbon Agent
     │
     ├── RAG Agent
     │
     └── Climate Agent
```

This allows different types of environmental questions to be processed by appropriate specialized modules.

---

## 📄 6. Document Analyzer

Users can upload environmental or climate-related PDF documents.

The Document Analyzer extracts text and uses IBM Granite to generate:

* document summary,
* important environmental information,
* risks or problems,
* recommended actions,
* important entities,
* locations,
* organizations mentioned in the document.

---

## 🖼️ 7. Image Analyzer

The Image Analyzer performs basic computer-vision preprocessing on uploaded environmental images.

It analyzes features such as:

* image dimensions,
* blue/cyan pixel percentage,
* green vegetation-like pixel percentage,
* image brightness.

These observations are passed to IBM Granite for environmental interpretation.

The system explicitly treats these observations as indicators rather than confirmed identification of water, vegetation, or flooding.

---

# 🧠 AI and ML Technologies

| Technology            | Purpose                               |
| --------------------- | ------------------------------------- |
| Python                | Core development                      |
| Streamlit             | Web application interface             |
| IBM Granite           | Natural-language generation           |
| IBM watsonx.ai        | Granite model access                  |
| Scikit-learn          | Machine Learning                      |
| Random Forest         | Flood-risk prediction                 |
| Sentence Transformers | Text embeddings                       |
| RAG                   | Knowledge-grounded question answering |
| Joblib                | ML model storage/loading              |
| OpenCV                | Computer vision                       |
| Pillow                | Image processing                      |
| PyPDF                 | PDF text extraction                   |
| Pandas                | Data processing                       |
| NumPy                 | Numerical operations                  |
| python-dotenv         | Environment configuration             |

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │      User Input      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Streamlit Web UI   │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
          Flood Risk          Carbon Tool       AI Chatbot
             │                    │                  │
             ▼                    ▼                  ▼
        ML Model             Calculation        IBM Granite
             │                                       │
             └──────────────────┬────────────────────┘
                                │
                                ▼
                         ┌────────────────┐
                         │  Agent Router  │
                         └───────┬────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
          RAG Agent         Document Agent     Image Agent
              │                  │                  │
              ▼                  ▼                  ▼
       Knowledge Base        PDF Text          Computer Vision
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 ▼
                         ┌────────────────┐
                         │  IBM Granite   │
                         └───────┬────────┘
                                 │
                                 ▼
                         ┌────────────────┐
                         │ User Response  │
                         └────────────────┘
```

---

# 📂 Project Structure

```text
ClimateGuard-AI/
│
└── climateguard_ai/
    │
    ├── app.py
    │
    ├── granite_service.py
    ├── prompts.py
    │
    ├── climate_chatbot.py
    ├── flood_risk.py
    ├── flood_ml.py
    ├── flood_model.pkl
    ├── train_flood_model.py
    │
    ├── carbon_calculator.py
    │
    ├── rag.py
    ├── rag_service.py
    │
    ├── agent_router.py
    ├── granite_router.py
    │
    ├── document_agent.py
    ├── image_agent.py
    │
    ├── documents/
    │   ├── climate_change.txt
    │   ├── flood_safety.txt
    │   ├── carbon_footprint.txt
    │   └── climate_actions.txt
    │
    ├── .streamlit/
    │   └── config.toml
    │
    ├── requirements.txt
    ├── .gitignore
    └── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/J2-66/ClimateGuard-AI.git
```

Move into the project directory:

```bash
cd ClimateGuard-AI/climateguard_ai
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

If PowerShell blocks activation, you can directly use Python from the environment without activating it.

---

## 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

# 🔐 Environment Variables

ClimateGuard AI uses IBM watsonx.ai credentials.

Create a `.env` file inside the project directory:

```env
WATSONX_APIKEY=YOUR_IBM_API_KEY
WATSONX_PROJECT_ID=YOUR_PROJECT_ID
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-4-h-small
```

### ⚠️ Security

**Never upload .env to GitHub.**

The `.gitignore` file should contain:

```gitignore
.env
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
uploaded_document.pdf
uploaded_image.jpg
```

Do not add:

```text
*.pkl
```

because `flood_model.pkl` is required by the deployed application.

---

# ▶️ Running the Application

From the `climateguard_ai` directory:

```powershell
python -m streamlit run app.py
```

The application will open in your browser.

If Streamlit does not open automatically, use the local URL displayed in the terminal.

---

# 🤖 Machine Learning Model

The Flood Risk Assistant uses a **Random Forest Classifier**.

### Input Features

```text
Rainfall
River Level
Waterlogging
Previous Flooding
Temperature
Humidity
```

The trained model is saved as:

```text
flood_model.pkl
```

The application loads the trained model using Joblib.

### Prediction Workflow

```text
Environmental Inputs
        │
        ▼
Feature Preparation
        │
        ▼
Random Forest Model
        │
        ▼
Risk Prediction
        │
        ▼
Prediction Probabilities
        │
        ▼
IBM Granite Explanation
```

The current model uses an educational dataset. Therefore, its output should not be interpreted as a real-world operational flood forecasting system.

---

# 📚 RAG Pipeline

The RAG system uses:

```text
Climate Documents
       │
       ▼
Text Extraction
       │
       ▼
Text Chunking
       │
       ▼
Sentence Transformer
       │
       ▼
Vector Embeddings
       │
       ▼
Cosine Similarity
       │
       ▼
Relevant Document Chunks
       │
       ▼
IBM Granite
       │
       ▼
Grounded Answer
```

The embedding model used is:

```text
sentence-transformers/all-MiniLM-L6-v2
```

---

# 🤖 Agentic AI Workflow

ClimateGuard AI uses specialized agents to handle different categories of questions.

### Available agents

**Flood Agent**

* Flood
* Rainfall
* River level
* Waterlogging
* Flood safety

**Carbon Agent**

* Carbon footprint
* CO₂ emissions
* Electricity
* Transportation
* Flights

**RAG Agent**

* Climate knowledge
* Climate documents
* Climate mitigation
* Climate adaptation
* Reference-based questions

**Climate Agent**

* General environmental and climate questions

The routing mechanism helps connect the user query to an appropriate specialized workflow.

---

# 📄 Document Analysis Workflow

```text
PDF Upload
    │
    ▼
PyPDF Text Extraction
    │
    ▼
Text Preprocessing
    │
    ▼
IBM Granite
    │
    ▼
Summary + Risks + Actions + Entities
```

The analyzer is designed for environmental and climate-related documents.

---

# 🖼️ Image Analysis Workflow

```text
Image Upload
     │
     ▼
OpenCV Processing
     │
     ├── Image Dimensions
     ├── Blue/Cyan Pixel Analysis
     ├── Green Pixel Analysis
     └── Brightness Analysis
             │
             ▼
       Structured Observations
             │
             ▼
        IBM Granite
             │
             ▼
    Environmental Interpretation
```

The image module performs basic computer-vision analysis rather than full image understanding.

---

# 🌱 Carbon Footprint Calculation

The application estimates emissions from:

```text
Electricity
     +
Car Travel
     +
Public Transportation
     +
Flights
     =
Estimated Monthly CO₂
```

The project uses predefined emission factors for educational estimation.

Because emission factors vary by location, energy source, vehicle, transportation type, and methodology, the results should be treated as approximate estimates.

---

# ⚠️ Safety and Limitations

ClimateGuard AI is an **educational AI project**.

### Flood Prediction

The flood model is not an official disaster-warning system.

It should not replace:

* government alerts,
* emergency services,
* meteorological information,
* local flood monitoring systems.

### Image Analysis

Color-based computer vision cannot reliably confirm:

* flooding,
* vegetation,
* geographical location,
* disaster severity,
* or other environmental conditions from an arbitrary image.

### Carbon Calculation

Carbon estimates depend on predefined emission factors and user inputs. Actual emissions may differ.

### AI Responses

IBM Granite responses can contain errors or incomplete information. Important environmental or safety decisions should be verified using authoritative local sources.

---

# ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

### Deployment steps

1. Push the project to GitHub.
2. Make sure `flood_model.pkl` is included in the repository.
3. Make sure `.env` is **not** included.
4. Open Streamlit Community Cloud.
5. Create a new application.
6. Select the GitHub repository.
7. Select branch:

```text
main
```

8. Set the main file:

```text
climateguard_ai/app.py
```

9. Add the IBM credentials through Streamlit Secrets.

Example:

```toml
WATSONX_APIKEY = "YOUR_IBM_API_KEY"
WATSONX_PROJECT_ID = "YOUR_PROJECT_ID"
WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
WATSONX_MODEL_ID = "ibm/granite-4-h-small"
```

10. Deploy the application.

### Important

Never place the IBM API key directly inside Python source code or commit it to GitHub.

---

# 🔮 Future Scope

The project can be extended with:

* Real-time weather API integration
* Real-time flood monitoring
* Geographic flood-risk mapping
* Satellite image analysis
* More advanced multimodal AI models
* Real environmental datasets
* Mobile application using Flutter
* Voice-based climate assistant
* Multilingual support
* Real-time carbon emission databases
* IoT-based environmental sensors
* Improved flood prediction using larger real-world datasets
* Advanced agentic workflows
* Automated environmental reports
* Location-aware climate recommendations

---

# 🌍 SDG Alignment

ClimateGuard AI supports several United Nations Sustainable Development Goals.

### SDG 13 — Climate Action

The project promotes climate awareness, climate education, emission reduction, and environmental risk awareness.

### SDG 11 — Sustainable Cities and Communities

Flood-risk awareness and environmental information can support safer and more resilient communities.

### SDG 12 — Responsible Consumption and Production

The carbon-footprint module helps users understand the environmental impact of electricity and transportation consumption.

### SDG 6 — Clean Water and Sanitation

Environmental and flood-related awareness can contribute to broader awareness of water-related environmental risks.

---

# 📊 Project Impact

ClimateGuard AI aims to make climate and environmental information easier to understand by combining several technologies into one platform.

Potential benefits include:

* Improved climate awareness
* Better understanding of carbon emissions
* Educational flood-risk awareness
* Easier access to climate knowledge
* AI-assisted environmental document analysis
* Basic environmental image interpretation
* Demonstration of practical AI/ML applications for sustainability

---

# 🧪 Technologies Used

```text
Python
│
├── Streamlit
├── IBM watsonx.ai
├── IBM Granite
├── Scikit-learn
├── Random Forest
├── Sentence Transformers
├── Retrieval-Augmented Generation
├── Agentic AI
├── OpenCV
├── Pillow
├── PyPDF
├── Pandas
├── NumPy
└── Joblib
```

---

# 📌 Project Status

**Status:** Completed / Deployed Prototype

The current version demonstrates the integration of:

* AI
* Machine Learning
* IBM Granite
* RAG
* Agentic AI
* Natural Language Processing
* Computer Vision
* Environmental calculations
* Streamlit web application development

---

# 👨‍💻 Author

**Mritunjoy Paul**

B.Tech — Computer Science and Engineering (Artificial Intelligence & Machine Learning)

### Areas of Interest

* Artificial Intelligence
* Machine Learning
* Data Science
* Generative AI
* Natural Language Processing
* Computer Vision
* Sustainable Technology

---

# 📜 License

This project is intended for educational and research purposes.

You may modify and extend the project according to your requirements while respecting the licenses of the third-party libraries, models, and services used.

---

# ⭐ Acknowledgements

This project makes use of open-source Python libraries and IBM watsonx.ai services.

Special acknowledgement to the developers and communities behind:

* IBM watsonx.ai
* IBM Granite
* Streamlit
* Scikit-learn
* Sentence Transformers
* OpenCV
* PyPDF
* Pandas
* NumPy

---

## 🌍 ClimateGuard AI

**AI for climate awareness, environmental understanding, and sustainable decision-making.**
