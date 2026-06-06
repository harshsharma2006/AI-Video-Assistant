import traceback
import streamlit as st
from dotenv import load_dotenv

from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarize import summarize, generate_title
from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions,
)
from core.rag_engine import build_rag_chain, ask_question

load_dotenv()

st.set_page_config(
    page_title="AI Video Assistant",
    page_icon="🎬",
    layout="wide"
)

if "result" not in st.session_state:
    st.session_state.result = None

st.title("🎬 AI Video Assistant")

source = st.text_input(
    "Enter YouTube URL or Local File Path"
)

language = st.selectbox(
    "Language",
    ["english", "hinglish"]
)

if st.button("Analyze"):

    if not source.strip():
        st.error("Please enter a URL or file path.")

    else:
        try:

            with st.spinner("Processing..."):

                chunks = process_input(source)

                transcript = transcribe_all(
                    chunks,
                    language
                )

                title = generate_title(transcript)

                summary = summarize(transcript)

                action_items = extract_action_items(transcript)

                decisions = extract_key_decisions(transcript)

                questions = extract_questions(transcript)

                rag_chain = build_rag_chain(transcript)

                st.session_state.result = {
                    "title": title,
                    "transcript": transcript,
                    "summary": summary,
                    "action_items": action_items,
                    "key_decisions": decisions,
                    "open_questions": questions,
                    "rag_chain": rag_chain,
                }

            st.success("Analysis Complete!")

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.code(traceback.format_exc())

if st.session_state.result:

    result = st.session_state.result

    st.header(result["title"])

    st.subheader("📋 Summary")
    st.write(result["summary"])

    st.subheader("✅ Action Items")
    st.write(result["action_items"])

    st.subheader("🔑 Key Decisions")
    st.write(result["key_decisions"])

    st.subheader("❓ Open Questions")
    st.write(result["open_questions"])

    st.subheader("📝 Transcript")

    st.text_area(
        "Transcript",
        result["transcript"],
        height=300
    )

    st.subheader("💬 Chat With Video")

    question = st.text_input(
        "Ask a question about the video"
    )

    if st.button("Ask") and question:

        answer = ask_question(
            result["rag_chain"],
            question
        )

        st.write(answer)