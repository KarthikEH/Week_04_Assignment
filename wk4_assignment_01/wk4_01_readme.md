Project: Agentic AI Architecture 
📌 Project Overview
This project demonstrates an automated pipeline for processing legal documents. It reads unstructured text files (like Rental Agreements) and uses Gemini 2.x/3.x to perform two key tasks:
1. Classification: Identifying the type of legal document (e.g., Rental Agreement, NDA, POA).
2. Information Extraction: Converting unstructured legal prose into structured JSON data for business automation.
🛠️ Tech Stack
* Language: Python 3.11
* AI Model: Google Gemini 1.5 Flash / 2.0 Flash (Native SDK)
* Frameworks: google-genai, python-dotenv
* Architecture: Direct API integration to bypass legacy library versioning conflicts.
🚀 Key Features
* JSON-First Output: The model is prompted to return valid JSON, making it ready for integration with databases or Excel.
* Safety Valve: Includes logic to categorize non-legal or irrelevant text as "Other."
* Real-World Ready: Successfully tested on a complex 1,000+ word Rental Agreement, extracting parties, rent amounts, and pet policies with 100% accuracy.
📁 File Structure
* wk4_lgl_doc_classifier.py: The core logic and extraction engine.
* test_text.txt: Sample input file used for verification.
* .env: (Ignored/Not uploaded) Stores the GOOGLE_API_KEY.
📈 Dev Log: Challenges Overcome
* Endpoint Evolution: Handled 404 NOT_FOUND errors by migrating from the LangChain wrapper to the native google.genai SDK to ensure compatibility with 2026 stable endpoints.
* Quota Management: Implemented model fallback strategies (switching between Flash 1.5 and 2.0) to manage 429 RESOURCE_EXHAUSTED errors on the free-tier API.

1. File List & Purpose
* wk4_lgl_doc_classifier.py: The main execution engine that reads the document, communicates with Gemini, and prints the structured JSON results.
* test_text.txt: The input file where we paste the raw legal text (like the Michael Thompson lease) to be analyzed by the AI.
* .env: A hidden configuration file that securely stores your GOOGLE_API_KEY so it isn't hardcoded in the script.
2. Code Breakdown (Imports & Functions)
Imports
* os: Used to access the computer's environment variables (like the API key).
* google.genai: The native Google SDK used to send prompts and receive responses from the Gemini models.
* dotenv (load_dotenv): Loads the variables from your .env file into the script's memory.
Functions
* client = genai.Client(...): Initializes the connection to Google using your credentials.
* classify_document(text): The core logic function that sends your specific prompt and the document text to the AI.
* client.models.generate_content(...): The specific call that tells the AI which model to use and what content to process.
* with open(file_path, "r") as f: The Python command used to open, read, and close your text file safely.
3. Hurdles & Solutions
* Hurdle 1: 404 NOT_FOUND: Legacy LangChain libraries were searching for "v1beta" endpoints that no longer exist for your model.
    * Solution: Switched from LangChain to the Native Google GenAI SDK to use stable 2026 endpoints.
* Hurdle 2: 429 RESOURCE_EXHAUSTED: Hit the Free-Tier rate limit for the new Gemini 2.0/3.0 models.
    * Solution: Switched to gemini-flash-latest and added a 60-second "cooldown" between runs.
* Warning/Precaution: Always check your model list. AI models are deprecated quickly; run a "list models" script if your code suddenly stops finding the AI.
4. Command Prompts Used
* source bin/activate: To enter your (demo_langchain) virtual environment so the correct libraries are available.
* pip install -U google-genai python-dotenv: Used to install and update the necessary tools for the project.
* python3 wk4_lgl_doc_classifier.py: The command used to run your script and see the results in the terminal.
* python3 -c "...": Used as a "sanity check" to list available models directly from the Google API when the main code failed.
5. Reference Guide for Future Use
Pro-Tip: If you ever move this code to a new computer, remember that the .env file and the venv folder don't travel with you. You must recreate the .env and run your pip install commands again to get the "engine" running in the new "garage."
