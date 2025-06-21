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
2. Add your .env file:
   ```bash
   OPENAI_API_KEY=your_openai_key_here
3. Run the app:
   ```bash
   python main.py
4. Type commands like:
   ```pgsql
   say hello to George
   add 5 and 6
5. Type quit to exit the assistant.

---

## 📁 Project 2: AI Resume Critiquer (Web App)

A Streamlit web app that uses OpenAI to analyze and give feedback on resumes. Upload a PDF or TXT resume and optionally specify the job role you're aiming for.

### 🔧 Features
- Upload `.pdf` or `.txt` resume files
- Optional job role input for more targeted feedback
- Uses GPT to analyze and suggest improvements
- Structured, easy-to-read feedback format

### 🛠️ Tech Stack
- Python
- Streamlit
- Open AI API (GPT-4o-mini)
- PyPDF2
- dotenv

### ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install streamlit openai python-dotenv PyPDF2
2. Add your .env file:
   ```bash
   OPENAI_API_KEY=your_openai_key_here
3. Run the app:
   ```bash
   streamlit run main.py
4. Upload your resume and click `Analyze Resume`

---

## 📁 Project 3: AI Image Classifier (Web App)

A lightweight Streamlit web app that uses TensorFlow's pre-trained MobileNetV2 model to classify images and display the top predictions.

### 🔧 Features
- Upload `.jpg` or `.png` images
- Image is resized and preprocessed for the model
- Displays top 3 classification predictions with confidence

### 🛠️ Tech Stack
- Python
- Streamlit
- TensorFlow (MobileNetV2)
- OpenCV
- Pillow (PIL)

### ▶️ How to Run
1. Install Dependencies:
   ```bash
   pip install streamlit tensorflow opencv-python pillow
2. Run the app:
   ```bash
   streamlit run main.py
3. Upload an image and click Classify Image to view predictions.

---

## 📌 Notes

- These projects are educational and can be expanded with advanced features like memory, logging, file input/output, authentication, and deployment.
- All API keys are stored securely using environment variables (`.env`) and should **never** be committed to version control.
- For best results:
  - Use high-quality PDFs or plaintext for resume analysis.
  - Use well-lit, centered images for the image classifier.
  - Ensure proper input formatting when interacting with the CLI agent.

 ## 👤 Author

Built by **Seth Paolo Salazar**

Feel free to connect, collaborate, or reach out with any questions!
