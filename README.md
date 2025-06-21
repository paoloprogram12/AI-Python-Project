# 🧠 AI Projects Portfolio

This repository contains a collection of beginner-friendly but powerful AI-based projects built using Python, LangChain, Streamlit, TensorFlow, and OpenAI. Each project showcases a different application of AI—from chatting with a custom agent, to resume review, to image classification.

---

## 📁 Project 1: LangGraph CLI AI Agent

A command-line AI assistant powered by LangChain and LangGraph that can respond to user input and execute custom tools like a calculator and greeting function.

### 🔧 Features
- CLI interaction with streaming AI responses
- Uses LangChain's `@tool` decorator to integrate functions
- Built-in tools:
  - `calculator(a, b)` – Adds two numbers
  - `say_hello(name)` – Greets the user

### 🛠️ Tech Stack
- Python
- LangChain
- LangGraph
- OpenAI API
- dotenv

### ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install langchain langgraph openai python-dotenv
