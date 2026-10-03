from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# System prompt
system_prompt = """
You are a helpful AI assistant for small-business owners.
Give practical, clear, and easy-to-understand answers.
Keep your answers concise unless the user asks for more detail.
"""

# Conversation history
conversation_history = []

# Clean basic interface
print("=" * 50)
print("           🤖 AI CHATBOT")
print("=" * 50)
print("Ask me anything!")
print("Type 'clear' to clear the conversation.")
print("Type 'exit' to close the chatbot.")
print("=" * 50)

# Chat loop
while True:

    # Get input from the user
    user_input = input("\nYou: ").strip()

    # Exit command
    if user_input.lower() == "exit":
        print("\nBot: Goodbye! 👋")
        break

    # Clear conversation command
    if user_input.lower() == "clear":
        conversation_history = []
        print("\nBot: Conversation cleared! 🗑️")
        continue

    # Check for empty input
    if not user_input:
        print("Bot: Please enter a message.")
        continue

    # Add user message to conversation history
    conversation_history.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    # Show loading message
    print("\nBot is thinking...")

    try:
        # Send conversation history + system prompt to Gemini
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=conversation_history,
            config={
                "system_instruction": system_prompt
            }
        )

        # Get AI response
        bot_response = response.text

        # Display AI response
        print("\nBot:", bot_response)

        # Add AI response to conversation history
        conversation_history.append({
            "role": "model",
            "parts": [{"text": bot_response}]
        })

    except Exception as e:
        print("\nBot: Sorry, something went wrong. Please try again.")