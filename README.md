# Mithra 🤝

**An Empathetic AI Companion for Seniors**

Mithra is a warm, conversational AI designed to provide genuine emotional support and companionship for adults aged 50 and older. Built with empathy-first principles, Mithra listens without judgment, validates feelings, and offers a safe space for meaningful conversation.

---

## ✨ Features

- **Empathy-Driven Conversations**: Every interaction prioritizes validation and understanding
- **Stigma-Free Support**: No clinical language or diagnosis—just caring, friend-like conversation
- **Memory-Enabled**: Remembers conversation context for more natural, flowing dialogue
- **Simple & Clear**: Plain language designed for accessibility
- **Powered by Groq**: Fast, efficient AI responses using state-of-the-art language models
- **Privacy-Focused**: Conversations stay local; no data stored beyond the session

---

## 🎯 Core Principles

1. **Empathy First** - Validate feelings before anything else
2. **Stigma-Free** - Never diagnose, analyze, or use clinical terms
3. **Simple & Clear** - Plain, everyday language
4. **Non-Judgmental** - Accept without criticism
5. **Conversational** - Natural, flowing dialogue

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- A free Groq API key ([get one here](https://console.groq.com/keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mithra.git
   cd mithra
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

### Run Mithra

```bash
python main.py
```

---

## ⚙️ Configuration

Mithra can be customized via environment variables in your `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Your Groq API key (required) | - |
| `MODEL_NAME` | AI model to use | `qwen/qwen3-32b` |
| `TEMPERATURE` | Response creativity (0.0-1.0) | `0.7` |

### Available Models

- `qwen/qwen3-32b` (default) - Balanced performance
- `mixtral-8x7b-32768` - High quality, larger context
- `llama-3.3-70b-versatile` - Most capable
- `gemma2-9b-it` - Lightweight and fast

---

## 💬 Usage

Once running, you can:

- **Chat naturally**: Just type your message and press Enter
- **Reset conversation**: Type `reset` to start fresh
- **Exit**: Type `quit` to end the session

### Example Conversation

```
You: I've been feeling pretty lonely lately

Mithra: That sounds really hard. I'm glad you're talking about it. 
        What's been the loneliest part for you?

You: My kids don't visit much anymore

Mithra: I can hear how much that matters to you. It's natural to miss 
        them when you don't see them as often. Have you been able to 
        talk with them about how you're feeling?
```

---

## 📁 Project Structure

```
mithra/
├── main.py                    # Main application & MithraAgent class
├── mithra_system_prompt.md    # System prompt documentation
├── requirements.txt           # Python dependencies
├── pyproject.toml            # Project metadata
├── .env.example              # Example environment configuration
├── .gitignore                # Git ignore rules
├── .python-version           # Python version specification
└── README.md                 # This file
```

---

## 🧠 How It Works

Mithra uses a **ReACT framework** internally for each response:

1. **THINK**: Reflects on the user's emotional state and needs
2. **ACT**: Decides on the best conversational approach
3. **RESPOND**: Delivers a warm, validating response

This process ensures every reply is thoughtful, empathetic, and grounded in what the user is experiencing.

---

## 🛡️ Privacy & Safety

- **No data storage**: Conversations are not saved between sessions
- **No diagnosis**: Mithra never provides medical or mental health diagnoses
- **Companion, not therapist**: For professional support, users should consult qualified professionals
- **API usage**: Messages are processed by Groq's API (see their [privacy policy](https://groq.com/privacy-policy/))

---

## 🤝 Contributing

Contributions are welcome! Whether it's:

- Improving the system prompt
- Adding new features
- Enhancing empathy patterns
- Fixing bugs
- Improving documentation

Please feel free to open issues or submit pull requests.

---

## 📝 License

This project is open source. Please add your preferred license (MIT, Apache 2.0, etc.).

---

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [Groq](https://groq.com/)
- Inspired by the need for accessible, stigma-free emotional support

---

## 📧 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/mithra/issues) page
2. Open a new issue if your problem isn't already listed
3. For Groq API issues, visit [Groq Console](https://console.groq.com/)

---

**Remember**: Mithra is a companion for emotional support and conversation. For mental health concerns or crises, please contact a qualified healthcare professional or crisis helpline.

---

*Made with ❤️ for seniors who deserve to feel heard*
