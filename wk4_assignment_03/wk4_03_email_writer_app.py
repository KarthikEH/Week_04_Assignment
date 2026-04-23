import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Import your custom modular components
from wk4_03_context_manager import load_business_context
from wk4_03_prompt_templates import get_email_prompt

# --- INITIALIZATION ---
load_dotenv()
st.set_page_config(page_title="Smart Email Architect", layout="wide")

# Configure Gemini with the alias validated in your environment
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    # Using 'gemini-flash-latest' as per your explicit requirement
    model = genai.GenerativeModel('gemini-flash-latest')
else:
    st.error("API Key not found. Please check your .env file.")

# Load Digital Prosperity Hub Context from your JSON foundation
context = load_business_context()

# Initialize session state so the draft persists during reruns
if "draft" not in st.session_state:
    st.session_state.draft = ""

# --- AREA 1: SIDEBAR (Draft Configuration) ---
with st.sidebar:
    st.title("1. Draft Configuration")
    if context:
        st.success("'wk4_03_business_context.json' Loaded")
    
    recipe = st.selectbox("Email Recipe", 
                        ["Supplier Negotiation", "Amazon Seller Support", "Customer Service", "Influencer Outreach", "Personal"])
    
    tone = st.radio("Writing Tone", ["Formal", "Friendly", "Urgent", "Persuasive", "Diplomatic"])
    
    language = st.selectbox("Language", ["English", "Tamil (தமிழ்)", "German"])
    
    format_type = st.radio("Output Format", ["Markdown", "Plain Text"])

# --- MAIN UI ---
st.header("📧 Digital Prosperity Hub: Smart Email Architect")

# --- AREA 2: YOUR INTENT ---
st.subheader("2. Your Intent")
col1, col2 = st.columns([1, 2])

with col1:
    recipient = st.text_input("Recipient Role/Name", placeholder="e.g., Jaipur Granites")

with col2:
    message = st.text_area("What is your core message? (Intent)", 
                          placeholder="e.g., The quote is too expensive. Reduce it to 3.5k or I go elsewhere.")

# THE GENERATION TRIGGER
if st.button("🚀 Generate Smart Draft", type="primary"):
    if message:
        with st.spinner("Analyzing intent and architecting draft..."):
            try:
                # --- SANITY CHECK LAYER ---
                sanity_prompt = f"""
                Analyze this user intent for a business email: "{message}"
                Is this intent clear and professional, or is it gibberish/nonsense?
                Reply ONLY with 'CLEAR' or 'GIBBERISH'.
                """
                sanity_check = model.generate_content(sanity_prompt).text.strip().upper()

                if "GIBBERISH" in sanity_check:
                    st.error("🛑 **Intent Unclear:** The input provided doesn't seem to contain a valid business message. Please provide a clear intent for Digital Prosperity Hub.")
                else:
                    # Proceed to full generation
                    full_prompt = get_email_prompt(recipe, tone, language, recipient, message, context)
                    response = model.generate_content(full_prompt)
                    st.session_state.draft = response.text
                    st.rerun()
            except Exception as e:
                st.error(f"Generation Error: {e}")
    else:
        st.warning("Please enter your core message (Intent) before generating.")

# --- AREA 3: AUGMENTED RESULT ---
st.divider()
st.subheader("3. Augmented Result")

if st.session_state.draft:
    # Logic to toggle between Markdown view and editable Text Area
    if format_type == "Markdown":
        st.markdown(st.session_state.draft)
    else:
        st.text_area("Generated Email:", value=st.session_state.draft, height=400)
    
    # --- SINGLE AGENTIC REFINEMENT LOOP ---
    with st.expander("Refine Draft", expanded=True):
        refinement_input = st.text_input("Want to change something?", 
                                         placeholder="e.g., 'Make it shorter'",
                                         key="refine_input_final")
        
        if st.button("Apply Refinement", key="refine_button_final"):
            if refinement_input:
                with st.spinner("Analyzing your instructions..."):
                    try:
                        # --- THE GUARDRAIL PROMPT ---
                        validation_prompt = f"""
                        Analyze the following user input intended to refine an email: "{refinement_input}"
                        
                        If the input is gibberish, nonsensical, or contains no actionable instructions, 
                        reply with exactly one word: 'INVALID'.
                        Otherwise, reply with 'VALID'.
                        """
                        
                        validation_check = model.generate_content(validation_prompt).text.strip().upper()

                        if "INVALID" in validation_check:
                            st.warning("⚠️ The instructions provided seem unclear or nonsensical. Please provide specific feedback (e.g., 'Make it shorter').")
                        else:
                            # Proceed with actual refinement if valid
                            refine_prompt = f"""
                            Update this email draft:
                            {st.session_state.draft}
                            
                            Based on these instructions: "{refinement_input}"
                            Maintain the signature for {context['user_profile']['company']}.
                            """
                            response = model.generate_content(refine_prompt)
                            st.session_state.draft = response.text
                            st.rerun()
                            
                    except Exception as e:
                        st.error(f"Refinement Error: {e}")
else:
    st.info("Your smart draft will appear here after you click 'Generate'.")