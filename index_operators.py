import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Pinecone Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not PINECONE_API_KEY or not PINECONE_INDEX_NAME or not GOOGLE_API_KEY:
    raise ValueError("Please set PINECONE_API_KEY, PINECONE_INDEX_NAME, and GOOGLE_API_KEY in your .env file")

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Initialize Embedding Model
embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

# Define the path to your knowledge_base
KNOWLEDGE_BASE_PATH = "knowledge_base"

def index_operators():
    # Assume index already exists and connect to it
    index = pc.Index(PINECONE_INDEX_NAME)

    print("Indexing operator markdown files...")
    for filename in os.listdir(KNOWLEDGE_BASE_PATH):
        if filename.endswith(".md"):
            filepath = os.path.join(KNOWLEDGE_BASE_PATH, filename)
            with open(filepath, 'r') as f:
                content = f.read()
                operator_name = filename.replace(".md", "")
                
                # Generate embedding for the content
                vector = embeddings_model.embed_query(content)
                
                # Upsert to Pinecone
                index.upsert(vectors=[{
                    "id": operator_name,
                    "values": vector,
                    "metadata": {"text": content, "operator_name": operator_name}
                }])
                print(f"Indexed {operator_name}")
    print("Indexing complete.")

if __name__ == "__main__":
    index_operators()
