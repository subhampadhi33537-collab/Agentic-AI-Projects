# 🎙️ Voice Agent with LangGraph & Groq (`openai/gpt-oss-120b`)

A real-time, hands-free conversational Voice Agent built inside a Jupyter Notebook (`main.ipynb`) using Python, LangChain, LangGraph, and Groq.

---

## 🔄 Architecture & Flow

```text
[ 🎤 Microphone ]
       │
       ▼  (Speech-to-Text via SpeechRecognition)
 [ User Voice Transcribed ]
       │
       ▼
┌───────────────────────────────────────────────┐
│             LangGraph Agent State             │
│  • Checkpointed Memory (MemorySaver)          │
│  • Multi-turn conversation context            │
│  • LLM: openai/gpt-oss-120b via Groq          │
└───────────────────────────────────────────────┘
       │
       ▼  (AI Response Text)
 [ Text-to-Speech via pyttsx3 ]
       │
       ▼
 [ 🔊 Speaker ]
```

---

## 🚀 Quick Start

1. Open [`main.ipynb`](file:///d:/COURSES/AIML/Mini%20Projects/Agentic%20AI%20Projects/Voice%20Agent/main.ipynb) in VS Code or Jupyter Notebook.
2. Run **Step 1** to install the required libraries:
   ```bash
   pip install -q langchain-groq langgraph langchain-core SpeechRecognition pyttsx3 pyaudio python-dotenv
   ```
3. Run **Step 2** to load the `GROQ_API_KEY` from your [`.env`](file:///d:/COURSES/AIML/Mini%20Projects/Agentic%20AI%20Projects/Voice%20Agent/.env).
4. Run **Step 3** to import the dependencies.
5. Run **Step 4** to initialize STT (`listen()`) and TTS (`speak()`).
6. Run **Step 5** to compile the LangGraph workflow with conversation memory (`MemorySaver`).
7. Run **Step 6** to start the continuous `while True` voice loop:
   - Speak into your microphone in English.
   - Say **`"exit"`**, **`"quit"`**, or **`"stop"`** to end the conversation at any time.
