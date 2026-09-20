
import streamlit as st

# ============================================================
# IMPORTS
# ============================================================

from rag_service import ask_rag
from granite_service import ask_granite
from climate_chatbot import climate_chat
from carbon_calculator import calculate_carbon_footprint
from prompts import CARBON_PROMPT

from agent_router import run_agent
from document_agent import analyze_document
from image_agent import analyze_image

from flood_ml import (
    predict_flood_risk,
    generate_flood_explanation
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ClimateGuard AI",
    page_icon="🌍",
    layout="wide"
)


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🌍 ClimateGuard AI")

st.write(
    "AI-powered environmental and climate awareness platform "
    "using IBM Granite, Machine Learning, RAG and AI Agents."
)

st.divider()


# ============================================================
# SIDEBAR NAVIGATION
# IMPORTANT:
# These names MUST match the conditions below.
# ============================================================

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🌊 Flood Risk Assistant",
        "🌱 Carbon Footprint",
        "💬 Climate Chatbot",
        "📚 Climate Knowledge RAG",
        "🤖 AI Agent",
        "📄 Document Analyzer",
        "🖼️ Image Analyzer"
    ]
)


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.header("🌍 Welcome to ClimateGuard AI")

    st.write(
        """
        ClimateGuard AI is an AI-powered environmental platform
        designed to provide climate awareness, flood-risk analysis,
        carbon-footprint estimation and climate knowledge assistance.
        """
    )

    st.subheader("🚀 Available Features")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            ### 🌊 Flood Risk Assistant

            Uses a machine-learning model to estimate educational
            flood-risk levels from environmental conditions such as:

            - Rainfall
            - River level
            - Waterlogging
            - Previous flooding
            - Temperature
            - Humidity
            """
        )

        st.markdown(
            """
            ### 🌱 Carbon Footprint

            Estimates monthly carbon emissions from:

            - Electricity usage
            - Car travel
            - Public transport
            - Flights
            """
        )

        st.markdown(
            """
            ### 💬 Climate Chatbot

            Ask general questions about:

            - Climate change
            - Environmental protection
            - Sustainability
            - Carbon emissions
            """
        )

    with col2:

        st.markdown(
            """
            ### 📚 Climate Knowledge RAG

            Uses Retrieval-Augmented Generation to search
            ClimateGuard AI's reference documents before generating
            an answer with IBM Granite.
            """
        )

        st.markdown(
            """
            ### 🤖 AI Agent

            Automatically selects a specialized agent for the
            user's question.
            """
        )

        st.markdown(
            """
            ### 📄 Document Analyzer

            Upload a climate or environmental PDF and generate
            an AI-powered analysis.
            """
        )

        st.markdown(
            """
            ### 🖼️ Image Analyzer

            Upload an environmental image for basic computer-vision
            analysis and AI interpretation.
            """
        )

    st.divider()

    st.info(
        "ClimateGuard AI is an educational project. "
        "Its flood-risk predictions and environmental estimates "
        "should not be treated as official emergency warnings "
        "or professional environmental assessments."
    )


# ============================================================
# FLOOD RISK ASSISTANT
# ============================================================

elif page == "🌊 Flood Risk Assistant":

    st.header("🌊 AI Flood Risk Prediction")

    st.write(
        "Enter environmental conditions to estimate flood risk "
        "using a machine-learning model."
    )

    st.info(
        "This is an educational machine-learning prediction "
        "and not an official emergency warning."
    )

    st.subheader("🌧️ Environmental Conditions")

    col1, col2 = st.columns(2)

    with col1:

        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            max_value=1000.0,
            value=100.0,
            step=10.0
        )

        river_level = st.slider(
            "River Level",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Very Low, 5 = Very High"
        )

        waterlogging = st.slider(
            "Waterlogging Level",
            min_value=0,
            max_value=3,
            value=1,
            help="0 = None, 1 = Minor, 2 = Moderate, 3 = Severe"
        )

    with col2:

        previous_flooding = st.selectbox(
            "Previous Flooding",
            ["No", "Yes"]
        )

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=-10.0,
            max_value=60.0,
            value=30.0,
            step=1.0
        )

        humidity = st.slider(
            "Humidity (%)",
            min_value=0,
            max_value=100,
            value=75
        )

    st.divider()

    if st.button(
        "🔍 Predict Flood Risk",
        use_container_width=True
    ):

        previous_flooding_value = (
            1 if previous_flooding == "Yes"
            else 0
        )

        try:

            with st.spinner(
                "Machine-learning model is predicting risk..."
            ):

                prediction, probabilities = predict_flood_risk(
                    rainfall=rainfall,
                    river_level=river_level,
                    waterlogging=waterlogging,
                    previous_flooding=previous_flooding_value,
                    temperature=temperature,
                    humidity=humidity
                )

            st.subheader("📊 ML Prediction")

            # ------------------------------------------------
            # DISPLAY PREDICTION
            # ------------------------------------------------

            if prediction == "High":

                st.error(
                    f"🚨 Predicted Flood Risk: {prediction}"
                )

            elif prediction == "Moderate":

                st.warning(
                    f"⚠️ Predicted Flood Risk: {prediction}"
                )

            else:

                st.success(
                    f"✅ Predicted Flood Risk: {prediction}"
                )

            # ------------------------------------------------
            # PROBABILITIES
            # ------------------------------------------------

            st.subheader("📈 Model Probabilities")

            for level, probability in probabilities.items():

                st.write(
                    f"**{level}: "
                    f"{probability * 100:.2f}%**"
                )

                st.progress(
                    min(max(float(probability), 0.0), 1.0)
                )

            # ------------------------------------------------
            # GRANITE EXPLANATION
            # ------------------------------------------------

            with st.spinner(
                "IBM Granite is preparing the explanation..."
            ):

                explanation = generate_flood_explanation(
                    rainfall=rainfall,
                    river_level=river_level,
                    waterlogging=waterlogging,
                    previous_flooding=previous_flooding_value,
                    temperature=temperature,
                    humidity=humidity,
                    prediction=prediction,
                    probabilities=probabilities
                )

            st.subheader(
                "🤖 ClimateGuard AI Explanation"
            )

            st.write(explanation)

            st.caption(
                "The prediction is generated from the educational "
                "Random Forest model trained for this project."
            )

        except Exception as e:

            st.error(
                f"An error occurred while predicting flood risk: {e}"
            )


# ============================================================
# CARBON FOOTPRINT
# ============================================================

elif page == "🌱 Carbon Footprint":

    st.header("🌱 Carbon Footprint Estimator")

    st.write(
        "Estimate your monthly carbon footprint from "
        "electricity, transportation and flights."
    )

    col1, col2 = st.columns(2)

    with col1:

        electricity = st.number_input(
            "Monthly electricity usage (kWh)",
            min_value=0.0,
            value=150.0,
            step=10.0
        )

        car_km = st.number_input(
            "Monthly car travel (km)",
            min_value=0.0,
            value=500.0,
            step=10.0
        )

    with col2:

        public_transport = st.number_input(
            "Monthly public transport travel (km)",
            min_value=0.0,
            value=100.0,
            step=10.0
        )

        flights = st.number_input(
            "Flights per month",
            min_value=0,
            value=0,
            step=1
        )

    st.divider()

    if st.button(
        "🌱 Calculate Carbon Footprint",
        use_container_width=True
    ):

        try:

            result = calculate_carbon_footprint(
                electricity,
                car_km,
                public_transport,
                flights
            )

            total = result["total"]

            st.subheader(
                "📊 Estimated Monthly Footprint"
            )

            st.metric(
                "Total CO₂",
                f"{total:.2f} kg"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"⚡ **Electricity:** "
                    f"{result['electricity']:.2f} kg CO₂"
                )

                st.write(
                    f"🚗 **Car:** "
                    f"{result['car']:.2f} kg CO₂"
                )

            with col2:

                st.write(
                    f"🚌 **Public Transport:** "
                    f"{result['public_transport']:.2f} kg CO₂"
                )

                st.write(
                    f"✈️ **Flights:** "
                    f"{result['flights']:.2f} kg CO₂"
                )

            # ------------------------------------------------
            # GRANITE ENVIRONMENTAL INSIGHTS
            # ------------------------------------------------

            prompt = CARBON_PROMPT.format(
                electricity=result["electricity"],
                transport=(
                    result["car"]
                    + result["public_transport"]
                ),
                other=result["flights"],
                total=total
            )

            with st.spinner(
                "IBM Granite is generating environmental insights..."
            ):

                explanation = ask_granite(
                    prompt,
                    max_new_tokens=250,
                    temperature=0.3
                )

            st.subheader(
                "🤖 AI Environmental Insights"
            )

            st.write(explanation)

            st.caption(
                "This is an educational estimate. Actual emissions "
                "depend on the emission factors and assumptions used."
            )

        except Exception as e:

            st.error(
                f"An error occurred while calculating emissions: {e}"
            )


# ============================================================
# CLIMATE CHATBOT
# ============================================================

elif page == "💬 Climate Chatbot":

    st.header("💬 Climate Awareness Chatbot")

    st.write(
        "Ask ClimateGuard AI questions about climate change, "
        "environment and sustainability."
    )

    question = st.text_area(
        "Enter your question",
        placeholder=(
            "Example: How can I reduce my carbon footprint?"
        ),
        height=120
    )

    if st.button(
        "💬 Ask ClimateGuard AI",
        use_container_width=True
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            try:

                with st.spinner(
                    "ClimateGuard AI is thinking..."
                ):

                    answer = climate_chat(
                        question
                    )

                st.subheader(
                    "🤖 ClimateGuard AI"
                )

                st.write(answer)

            except Exception as e:

                st.error(
                    f"An error occurred: {e}"
                )


# ============================================================
# RAG KNOWLEDGE ASSISTANT
# ============================================================

elif page == "📚 Climate Knowledge RAG":

    st.header("📚 Climate Knowledge Assistant")

    st.write(
        "Ask questions using ClimateGuard AI's environmental "
        "knowledge documents."
    )

    question = st.text_area(
        "Ask a question",
        placeholder=(
            "Example: What should I do during a flood?"
        ),
        height=120
    )

    if st.button(
        "🔎 Search Knowledge Base",
        use_container_width=True
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            try:

                with st.spinner(
                    "Searching climate knowledge..."
                ):

                    answer, sources = ask_rag(
                        question
                    )

                st.subheader(
                    "🤖 ClimateGuard AI"
                )

                st.write(answer)

                st.subheader(
                    "📚 Retrieved Sources"
                )

                if sources:

                    for source in sources:

                        st.write(
                            f"**{source['filename']}** "
                            f"(similarity: "
                            f"{source['score']:.3f})"
                        )

                        with st.expander(
                            "View retrieved information"
                        ):

                            st.write(
                                source["text"]
                            )

                else:

                    st.info(
                        "No relevant documents were retrieved."
                    )

            except Exception as e:

                st.error(
                    f"An error occurred while searching the "
                    f"knowledge base: {e}"
                )


# ============================================================
# AI AGENT
# ============================================================

elif page == "🤖 AI Agent":

    st.header("🤖 ClimateGuard AI Agent")

    st.write(
        "Ask a question and ClimateGuard AI will automatically "
        "select a specialized agent."
    )

    st.info(
        """
        Available agents:

        • 🌊 Flood Agent
        • 🌱 Carbon Agent
        • 📚 RAG Agent
        • 💬 Climate Agent
        """
    )

    question = st.text_area(
        "Ask your question",
        placeholder=(
            "Example: What should I do during a flood?"
        ),
        height=120
    )

    if st.button(
        "🤖 Run AI Agent",
        use_container_width=True
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            try:

                with st.spinner(
                    "AI Agent is analyzing your question..."
                ):

                    result = run_agent(
                        question
                    )

                st.success(
                    f"Selected Agent: {result['agent']}"
                )

                st.subheader(
                    "🤖 ClimateGuard AI Response"
                )

                st.write(
                    result["response"]
                )

            except Exception as e:

                st.error(
                    f"An error occurred while running "
                    f"the AI Agent: {e}"
                )


# ============================================================
# DOCUMENT ANALYZER
# ============================================================

elif page == "📄 Document Analyzer":

    st.header("📄 Climate Document Analyzer")

    st.write(
        "Upload a climate or environmental PDF and let "
        "ClimateGuard AI analyze it."
    )

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success(
            f"Uploaded: {uploaded_file.name}"
        )

        if st.button(
            "📄 Analyze Document",
            use_container_width=True
        ):

            try:

                temp_path = "uploaded_document.pdf"

                with open(
                    temp_path,
                    "wb"
                ) as file:

                    file.write(
                        uploaded_file.getbuffer()
                    )

                with st.spinner(
                    "ClimateGuard AI is analyzing the document..."
                ):

                    result = analyze_document(
                        temp_path
                    )

                st.subheader(
                    "🤖 ClimateGuard AI Analysis"
                )

                st.write(result)

            except Exception as e:

                st.error(
                    f"An error occurred while analyzing "
                    f"the document: {e}"
                )


# ============================================================
# IMAGE ANALYZER
# ============================================================

elif page == "🖼️ Image Analyzer":

    st.header("🖼️ Climate Image Analyzer")

    st.write(
        "Upload an environmental image and let ClimateGuard AI "
        "perform basic computer-vision analysis."
    )

    st.info(
        "The current image analyzer uses computer-vision "
        "features such as color and brightness. It does not "
        "directly perform general image understanding."
    )

    uploaded_image = st.file_uploader(
        "Upload an environmental image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image is not None:

        st.success(
            f"Uploaded: {uploaded_image.name}"
        )

        st.image(
            uploaded_image,
            caption="Uploaded Environmental Image",
            use_container_width=True
        )

        if st.button(
            "🖼️ Analyze Image",
            use_container_width=True
        ):

            try:

                temp_image_path = "uploaded_image.jpg"

                with open(
                    temp_image_path,
                    "wb"
                ) as file:

                    file.write(
                        uploaded_image.getbuffer()
                    )

                with st.spinner(
                    "ClimateGuard AI is analyzing the image..."
                ):

                    result = analyze_image(
                        temp_image_path
                    )

                st.subheader(
                    "🤖 ClimateGuard AI Analysis"
                )

                st.write(result)

            except Exception as e:

                st.error(
                    f"An error occurred while analyzing "
                    f"the image: {e}"
                )


