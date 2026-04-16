import google.generativeai as genai
from config import GEMINI_API_KEY
from services.embedding import get_embedding_model
from services.pinecone_service import query_vectors

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def run_rag(question):
    embeddings = get_embedding_model()
    query_vector = embeddings.embed_query(question)

    results = query_vectors(query_vector)
    results = query_vectors(query_vector)

    context = "\n\n---\n\n".join(
        [m["metadata"]["text"] for m in results["matches"]]
    )

    prompt = f"""
You are an AI Resume Analyzer.

Context:
{context}

Question:
{question}

Tasks:
1. ATS score
2. Missing skills
3. Suggestions
"""

    response = model.generate_content(prompt)
    return response.text