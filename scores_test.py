from rag import load_index,search
import ollama
documents = load_index()


questions = [
    # aloqador
    "How much did Malika Yusupova's trip cost?",
    "Who was responsible for legal matters?",
    "What was the total cost of the trip?",
    "How many meetings were held?",
    "What was the hotel cost per person?",
    # aloqasiz
    "What is the capital of France?",
    "What is the weather like in London?",
    "Who won the football world cup?",
]

for q in questions:
    results = search(q, documents)
    print(q)
    for score, doc in results:
        print(f" {score:.3f} {doc['source']}")

