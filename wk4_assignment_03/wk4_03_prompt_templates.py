def get_email_prompt(recipe, tone, language, recipient, message, business_context):
    """Constructs the master prompt for the Gemini model."""
    
    # Extract identity details
    user = business_context.get("user_profile", {})
    biz = business_context.get("business_details", {})
    
    system_persona = f"""
    You are an expert AI Business Assistant for {user.get('name')}, the {user.get('role')} of {user.get('company')}.
    Your business focus is {biz.get('primary_focus')} based in {biz.get('location')}.
    Your goal is to draft a high-quality email that reflects the owner's professional brand.
    """
    
    instructions = f"""
    TASK: Write a {recipe} email.
    RECIPIENT: {recipient}
    TONE: {tone}
    LANGUAGE: Write the entire response in {language}.
    CORE MESSAGE: {message}
    
    GUIDELINES:
    1. Use a professional opening and closing.
    2. Incorporate business context naturally.
    3. Ensure the tone is strictly {tone}.
    4. End with the following signature:
    ---
    {user.get('signature')}
    """
    
    return system_persona + instructions