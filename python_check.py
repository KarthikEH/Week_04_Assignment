# A simple logic check for your first Agent Practice
def agent_response(input_text):
    if "hello" in input_text.lower():
        return "Agent: Hello! I am ready to help with LangChain."
    return "Agent: I'm listening..."

user_query = "Hello there!"
print(agent_response(user_query))