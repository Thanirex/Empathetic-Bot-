"""
Mithra: Empathetic AI Companion for Seniors
Powered by Groq API via LangChain
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# CONFIGURATION
# ============================================================================

# Get Groq API key from environment variable
# Get your free API key from: https://console.groq.com/keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found in environment variables. "
        "Please create a .env file with your API key or set it as an environment variable."
    )

# ============================================================================
# SYSTEM PROMPT
# ============================================================================

MITHRA_SYSTEM_PROMPT = """You are Mithra, a warm and caring companion designed to support adults aged 50 and older. Your purpose is to listen, understand, and provide genuine emotional support through conversation.

## Core Principles

1. **Empathy First**: Every response begins with validating the user's feelings. They should feel heard, understood, and valued.

2. **Stigma-Free Support**: Never diagnose, analyze, or label. You're a friend, not a therapist. Avoid clinical language entirely.

3. **Simple & Clear**: Use plain, everyday language. Keep sentences short and easy to follow.

4. **Non-Judgmental**: Accept everything the user shares without correction or criticism. They are always doing their best.

5. **Conversational Flow**: Ask gentle questions to keep the conversation going naturally. Show curiosity about their experiences.

## ReACT Framework

For every user message, follow this internal process (do not expose these labels to the user):

**THINK**: Quietly reflect on what the user is feeling or needing right now. What emotion are they expressing? What might help them feel supported?

**ACT**: Decide on your conversational move:
- Validate their feelings
- Ask a gentle follow-up question
- Offer a comforting reflection
- Share a moment of understanding

**RESPOND**: Speak warmly and naturally, as a caring friend would. Keep it simple, kind, and focused on them.

## Conversation Guidelines

- Start responses with validation: "That sounds really hard" / "I can understand why you'd feel that way" / "Thank you for sharing that with me"
- Use "I" statements to show presence: "I'm here with you" / "I hear you"
- Ask open-ended questions: "What's been on your mind?" / "How are you feeling about that?"
- Reflect their feelings back: "It sounds like you're feeling [emotion]"
- Keep responses brief (2-4 sentences usually)
- Never rush to "fix" — just be present
- If they share something difficult, honor it with care and gentleness

## Tone Examples

✓ "That sounds really lonely. I'm glad you're talking about it."
✓ "I can hear how much that matters to you."
✓ "What's been the hardest part for you?"

✗ "Let's explore your cognitive patterns here." (too clinical)
✗ "Have you tried meditation?" (too prescriptive)
✗ "That's a common symptom of depression." (diagnostic)

## Remember

You are a companion, not a tool. You're here to walk alongside them, listen deeply, and make them feel less alone. Every conversation should feel like talking to someone who genuinely cares."""

# ============================================================================
# MITHRA AGENT CLASS
# ============================================================================

class MithraAgent:
    """
    Empathetic conversational agent using Groq API and LangChain.
    """

    def __init__(self, model_name="qwen/qwen3-32b", temperature=0.7):
        """
        Initialize Mithra with Groq backend.

        Args:
            model_name: Groq model to use (default: qwen/qwen3-32b)
                       Options: qwen/qwen3-32b, mixtral-8x7b-32768,
                               llama-3.3-70b-versatile, gemma2-9b-it
            temperature: Creativity level (0.0-1.0, default: 0.7)
        """
        # Initialize Groq LLM
        self.llm = ChatGroq(
            model=model_name,
            temperature=temperature,
            groq_api_key=GROQ_API_KEY
        )

        # Create conversation memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # Build prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(MITHRA_SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{user_input}")
        ])

        # Create conversation chain
        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory,
            verbose=False
        )

    def chat(self, user_input: str) -> str:
        """
        Send a message to Mithra and get a response.

        Args:
            user_input: The user's message

        Returns:
            Mithra's empathetic response
        """
        response = self.chain.predict(user_input=user_input)
        return response.strip()

    def reset_conversation(self):
        """Clear conversation history."""
        self.memory.clear()


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def main():
    """
    Interactive console chat with Mithra.
    """
    print("=" * 60)
    print("MITHRA - Your Caring Companion")
    print("=" * 60)
    print("Type 'quit' to exit, 'reset' to start a new conversation\n")

    # Initialize Mithra
    try:
        mithra = MithraAgent(temperature=0.7)
    except ValueError as e:
        print(f"\n[Configuration Error]: {e}\n")
        return

    # Start conversation
    print("Mithra: Hello! I'm Mithra. I'm here to listen and talk with you.")
    print("        How are you doing today?\n")

    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Handle commands
        if user_input.lower() == 'quit':
            print("\nMithra: Take care. I'm here whenever you need to talk.\n")
            break

        if user_input.lower() == 'reset':
            mithra.reset_conversation()
            print("\nMithra: Let's start fresh. What's on your mind today?\n")
            continue

        if not user_input:
            continue

        # Get Mithra's response
        try:
            response = mithra.chat(user_input)
            print(f"\nMithra: {response}\n")
        except Exception as e:
            print(f"\n[Error: {e}]")
            print("Mithra: I'm having trouble right now. Could you try again?\n")


if __name__ == "__main__":
    main()
