from pinecone import Pinecone
from config import PINECONE_API_KEY, PINECONE_INDEX

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

def upsert_vectors(chunks, embeddings):
    vectors = []
    for i, doc in enumerate(chunks):
        vector = embeddings.embed_query(doc.page_content)
        vectors.append({
            "id": f"vec-{i}",
            "values": vector,
            "metadata": {"text": doc.page_content}
        })
        index.upsert(vectors)


def query_vectors(query_vector):
    return index.query(
        vector=query_vector,
        top_k=5,
        include_metadata=True
    )
