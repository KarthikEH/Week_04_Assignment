Digital Prosperity Hub: AI Legal Assistant, is a professional-grade web dashboard designed to automate the extraction of critical terms from complex legal documents. By combining the Gemini 2.0 Flash model with a Streamlit interface, it transforms unstructured rental agreements into structured, business-ready data with built-in guardrails for accuracy and reliability.

1. File Directory Overview
Here is a breakdown of the key files visible in your VS Code explorer:
* wk4_02_ui_assistant.py: The core application file containing the Streamlit interface and Gemini AI logic.
* .env: Stores your sensitive GOOGLE_API_KEY to keep it out of the public code.
* wk4_01_test_contract.txt: The original test document used to verify the AI's extraction accuracy.
* wk4_02_rental_img01/02.jpg: Visual assets (screenshots) of the UI for documentation purposes.
* wk4_02_sample_agreement01/02.md: Text-based templates used to test the model's performance on different contract formats.
* .gitignore: Instructs Git to ignore environment files and virtual environments (bin/, lib/) so they aren't pushed to GitHub.
* tempCodeRunnerFile.py: A temporary file created by VS Code when using the "Run Code" button; safe to ignore or delete.
2. Code Breakdown (Imports & Functions)
Imports:
* streamlit as st: Powering the web dashboard and layout elements (buttons, sidebars, tables).
* os: Accessing the operating system to retrieve the API key from your environment.
* json: Parsing the AI's string output into a structured format for the UI table.
* google.genai: The 2026 SDK used to communicate with the Gemini 2.0 Flash model.
* dotenv (load_dotenv): Loading local variables from your .env file into the script.
Functions:
* analyze_document(text_content): Sends document text to Gemini with specific JSON instructions and returns the cleaned data.
* st.file_uploader(): Handles the secure upload of .txt files from your MacBook.
* st.metric() & st.table(): Displays the extracted "Rent" and "Landlord" data in a professional dashboard format.
3. Hurdles, Solutions, and Takeaways
* Hurdle 1: API Version Shift: Teammates encountered errors with outdated get_transcript methods.
    * Solution: Moved to the 2026 object-oriented .fetch() method in the latest SDK.
* Hurdle 2: Encoding Errors: Files containing special characters (like curly quotes) caused the app to crash during upload.
    * Solution: Switched from utf-8 to latin-1 decoding to handle non-standard text symbols gracefully.
* Hurdle 3: 503 Service Unavailable: The AI model briefly hit capacity limits during high-demand periods.
    * Solution: Implemented a retry strategy and error-handling blocks to inform the user instead of crashing.
* Takeaway/Warning: Always validate AI output as JSON before attempting to display it; "Hallucinated" or malformed JSON is the #1 cause of UI failure in Agentic AI.
4. Command Prompts Used
* pip install -U google-genai streamlit python-dotenv: Run once to set up the necessary libraries in your (demo_langchain) environment.
* streamlit run wk4_02_ui_assistant.py: Used every time you want to launch the local web server and view the UI in your browser.
* ls: Used to verify file names and ensure the correct file path was being targeted.
* git remote set-url origin [URL]: Used to point your local folder to the new, clean GitHub repository you created.
* git push -u origin main: Used to upload your final, organized code to the cloud for submission.
5. Suggested readme.md Structure
You can copy this directly into a new text file:
# Project: Digital Prosperity Hub - AI Legal Assistant
Purpose: A professional Streamlit dashboard that extracts rental terms (Landlord, Tenant, Rent, Dates) from unstructured text files using Gemini 2.0.
Setup:
1. Ensure .env contains a valid Google API Key.
2. Run pip install -r requirements.txt.
3. Launch via streamlit run wk4_02_ui_assistant.py.
Key Architect Decisions:
* Used Latin-1 encoding to ensure compatibility with varied document sources.
* Implemented Negative Testing with a Dosa Recipe to ensure the AI only extracts relevant legal data.