import streamlit as st
import os
import json
import google.genai as genai
from dotenv import load_dotenv

# 1. INITIAL SETUP & CONFIGURATION
load_dotenv()
st.set_page_config(
    page_title="Digital Prosperity Hub | AI Legal Assistant",
    page_icon="📄",
    layout="wide"
)

# Initialize the Gemini Client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. THE AI EXTRACTION ENGINE
def analyze_document(text_content):
    """
    Sends document text to Gemini and returns structured JSON data.
    """
    prompt = f"""
    Analyze the following document. Extract data into a valid JSON format with these exact keys:
    'category', 'rent_amount', 'landlord_name', 'tenant_name', 'start_date', 'end_date', 'pet_allowed'.
    
    Rules:
    - If it's a Rental Agreement, extract the values.
    - If it's NOT a rental agreement/contract, set 'category' to 'Other' and all other fields to null.
    - Return ONLY the raw JSON string.

    Text: {text_content}
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest", 
            contents=prompt
        )
        
        # Clean the response: Gemini sometimes wraps JSON in ```json blocks
        raw_text = response.text
        clean_json_str = raw_text.replace("```json", "").replace("```", "").strip()
        
        return json.loads(clean_json_str)
    
    except Exception as e:
        st.error(f"AI Processing Error: {e}")
        return None

# 3. STREAMLIT UI LAYOUT
st.title("📄 Digital Prosperity Hub: Legal Assistant")
st.markdown("---")

# Sidebar for controls
st.sidebar.header("Document Control Center")
uploaded_file = st.sidebar.file_uploader("Upload a Contract (.txt)", type=['txt'])

if uploaded_file is not None:
    # Read the uploaded file
    file_content = uploaded_file.read().decode("latin-1")
    
    # Create two columns: Left for Raw Text, Right for AI Analysis
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📜 Document Preview")
        st.text_area("Content from file:", file_content, height=450)
        
    with col2:
        st.subheader("🤖 AI Smart Extraction")
        
        if st.button("Run Legal Analysis", type="primary"):
            with st.spinner("Analyzing clauses and extracting terms..."):
                data = analyze_document(file_content)
                
                if data:
                    # Top Metrics for quick glancing
                    m_col1, m_col2 = st.columns(2)
                    m_col1.metric("Doc Type", data.get('category', 'Unknown'))
                    
                    # Formatting rent display
                    rent = data.get('rent_amount')
                    rent_display = f"${rent}" if rent else "N/A"
                    m_col2.metric("Monthly Rent", rent_display)
                    
                    st.markdown("---")
                    
                    # Detailed Table
                    st.write("#### Detailed Extraction Results")
                    st.table(data)
                    
                    # Success message
                    st.success("Analysis Complete. Data is ready for export.")
                else:
                    st.error("Failed to parse document data.")
else:
    # Landing state when no file is uploaded
    st.info("👋 Welcome, Karthik. Please upload a document in the sidebar to begin the analysis.")
    st.image("https://img.icons8.com/clouds/500/contract.png", width=200)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Powered by Gemini 2.0 Flash & Streamlit")