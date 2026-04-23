import langchain
import langchain_community
import langgraph
from dotenv import load_dotenv
import os

print("--- Environment Check ---")
print(f"LangChain Version: {langchain.__version__}")
print(f"LangGraph Version: {langgraph.__version__}")

# Check for .env file
if os.path.exists(".env"):
    print("✅ .env file found")
else:
    print("⚠️ .env file missing (You'll need this for API keys!)")

print("-------------------------")
print("Environment is officially ready for Agent AI Architecture!")