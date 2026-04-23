import os
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()

# Direct client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def classify_document(text):
    prompt = f"""
    Analyze the following contract. Extract the data into a valid JSON format with these keys:
    'category', 'rent_amount', 'landlord_name', 'tenant_name', 'start_date', 'end_date', 'pet_allowed'.
    
    If it's not a contract, set category to 'Other' and other fields to null.

    Text: {text}
    """
      
    # Using the most stable alias
    response = client.models.generate_content(
        model="gemini-flash-latest", 
        contents=prompt
    )
    # The fix is right here: .text
    return response.text.strip()

if __name__ == "__main__":
    # 1. Path to your text file
    file_path = "wk4_01_test_contract.txt"
    
    try:
        # 2. Read the contents of the file
        with open(file_path, "r") as f:
            content = f.read()
        
        # 3. Pass that content to the classifier
        result = classify_document(content)
        
        print(f"--- FILE TEST SUCCESS ---")
        print(f"File Content: {content}")
        print(f"Detected Type: {result}")
        
    except FileNotFoundError:
        print(f"Bollocks! I can't find {file_path}")
    except Exception as e:
        print(f"Machine says: {e}")