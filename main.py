from utils.loader import load_pdf
from utils.chunker import split_docs
from services.embedding import get_embedding_model
from services.pinecone_service import upsert_vectors
from services.query_rewriter import rewrite_query
from services.rag_pipeline import run_rag


def index_resume():
    docs = load_pdf("./resume.pdf")
    chunks = split_docs(docs)

    embeddings = get_embedding_model()
    upsert_vectors(chunks, embeddings)

    print("Resume indexed successfully")
    def main():
        print("Indexing resume...")
        index_resume()

        while True:
            question = input("Ask about resume --> ")
            rewritten = rewrite_query(question)
            answer = run_rag(rewritten)
            print("\n===== RESULT =====\n")
            print(answer)


    if __name__ == "__main__":
        main()