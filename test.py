from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarize import summarize, generate_title
from core.rag_engine import build_rag_chain

url = input("Enter YouTube URL: ")

# Download + Transcribe
chunks = process_input(url)
transcript = transcribe_all(chunks)

print("\n===== TRANSCRIPT =====\n")
print(transcript)

# Summary
title = generate_title(transcript)
summary = summarize(transcript)

print("\n===== TITLE =====\n")
print(title)

print("\n===== SUMMARY =====\n")
print(summary)

# Build RAG
rag_chain = build_rag_chain(transcript)

print("\nRAG Ready! Ask questions about the video.")
print("Type 'exit' to quit.\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        break

    answer = rag_chain.invoke(question)

    print("\nAnswer:")
    print(answer)
    print()