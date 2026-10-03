AI Chatbot

Built

A basic AI chatbot developed in Python using the Google Gemini API.

The chatbot can:

- Accept user messages
- Generate AI responses using Gemini
- Maintain conversation history
- Clear the conversation when requested
- Handle empty user input
- Show a loading message while generating a response
- Handle API/runtime errors
- Use a system prompt to define the assistant's role and response style

Technology Used

- Python 3.12
- Google Gemini API
- "google-genai"
- "python-dotenv"
- Git and GitHub

How to Run

1. Clone this repository.
2. Install the required packages:

pip install -r requirements.txt

3. Create a ".env" file in the project folder.
4. Add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

5. Run the chatbot:

python chatbot.py

API Integration

The chatbot uses the Google Gemini API through the "google-genai" Python package.

The API key is stored in a ".env" file and loaded using "python-dotenv". The API key is not included in the GitHub repository.

The chatbot sends the user's message and conversation history to the Gemini model and displays the generated response.

Conversation Features

The chatbot maintains conversation history during the session, allowing follow-up questions based on previous messages.

The user can type:

- "clear" — clears the current conversation history
- "exit" — closes the chatbot

What I Learned

Through this project, I learned:

- How to integrate an AI API into a Python application
- How to use environment variables to protect API keys
- How to use Git and GitHub for version control
- How to maintain conversation history
- How to implement basic error handling
- How to create a simple command-line chatbot interface
- How to use a system prompt to control the chatbot's behavior

Future Improvements

Possible future improvements include:

- Web-based user interface
- Markdown response formatting
- Voice input and output
- Persistent conversation history
- More advanced memory/context handling
- Improved user interface and experience