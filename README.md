# 🎬 AI Video Assistant

An AI-powered application that analyzes YouTube videos and local video files to generate transcripts, summaries, action items, key decisions, and answer questions using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

* 🎙️ Speech-to-Text Transcription using OpenAI Whisper
* 📝 AI-Powered Video Summarization
* ✅ Action Item Extraction
* 🔑 Key Decision Detection
* ❓ Open Question Identification
* 💬 Chat with Video (RAG)
* 📺 YouTube Video Support
* 📂 Local Video File Support
* 🌐 Interactive Streamlit Interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI Whisper
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Mistral AI
* yt-dlp
* FFmpeg

---

## 📂 Project Structure

```text
AI-Video-Assistant/
│
├── core/
│   ├── extractor.py
│   ├── rag_engine.py
│   ├── summarize.py
│   ├── transcriber.py
│   └── vector_store.py
│
├── utils/
│   └── audio_processor.py
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Workflow

```text
Video Input
      │
      ▼
Audio Extraction
      │
      ▼
Whisper Transcription
      │
      ▼
Transcript Generation
      │
      ▼
Vector Database (ChromaDB)
      │
      ▼
RAG Pipeline (LangChain)
      │
      ▼
Mistral AI
      │
      ▼
Summary + Q&A + Insights
```

---

## ▶️ Installation

```bash
git clone https://github.com/harshsharma2006/AI-Video-Assistant.git

cd AI-Video-Assistant

pip install -r requirements.txt
```

---

## ⚙️ Environment Setup

Create a `.env` file in the project root with your Mistral API key (and ensure `FFmpeg` is installed on your system):

```env
MISTRAL_API_KEY=your_mistral_api_key_here
WHISPER_MODEL=base
```

## ▶️ Run Application

```bash
# Primary custom-styled Streamlit interface
streamlit run app.py

# Or minimal interface
streamlit run main.py
```

---

## 🎯 Use Cases

* Meeting Analysis
* Educational Video Summarization
* Content Research
* Knowledge Extraction
* AI-Powered Video Q&A
* Lecture & Webinar Analysis
* Learning Assistant

---

## 🔮 Future Enhancements

* Multi-language Support
* PDF Report Generation
* Cloud Deployment
* Speaker Identification
* Real-Time Video Analysis
* Advanced Analytics Dashboard

---

## 👨‍💻 Developer

**Harsh Sharma**

Data Science Undergraduate | Generative AI Enthusiast | Building AI-Powered Solutions with Python, LangChain, Vector Databases, and Large Language Models.

🚀 Passionate about Artificial Intelligence, Machine Learning, Data Science, and creating real-world AI applications that transform data into actionable insights.

📍 Lingaya's Vidyapeeth, Faridabad, India

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
