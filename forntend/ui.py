import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="MycoGuard Swarm UI", page_icon="🍄", layout="wide")

st.title("🍄 MycoGuard: Live Cloud Connection")
st.markdown("Upload your requirements and summon the Google Cloud Agent Swarm to architect your secure code!")

# --- CONFIGURATION ---
# Ensure there are no leading spaces in the URL string
API_URL = "Enter your NGROK link here"

# User Input
query = st.text_input(
    "What should the Swarm do?", 
    value="Clean the data, train a random forest model, and strictly validate for false negatives."
)

if st.button("🚀 Summon Cloud Agent Swarm"):
    with st.spinner("🧠 Connecting to Google Colab... Please wait while Agents generate your code..."):
        
        # Prepare the payload for the backend
        payload = {"query": query}
        
        try:
            # Initiating the HTTP POST request to your FastAPI/Ngrok endpoint
            response = requests.post(API_URL, json=payload, timeout=120) 
            
            if response.status_code == 200:
                data = response.json()
                st.success("✅ Code generation complete! Response received from Cloud Agents.")
                
                st.subheader("📄 Generated Executable Code:")
                # Display the real code returned from the backend
                st.code(data["generated_code"], language="python")
                
            else:
                st.error(f"Cloud Server Error. Status Code: {response.status_code}")
                st.info("Tip: Check if your FastAPI server is still active in Colab.")
                
        except Exception as e:
            st.error("🚨 Network Connection Failed!")
            st.markdown(f"""
            **Please verify the following:**
            1. Is the **FastAPI** server running in your Colab notebook?
            2. Is the **Ngrok URL** (`{API_URL}`) still active and copied correctly?
            3. Is your internet connection stable?
            
            **Error Details:** `{e}`
            """)

# Optional Footer
st.divider()
st.caption("Powered by MycoGuard Swarm Intelligence & Google Colab")
