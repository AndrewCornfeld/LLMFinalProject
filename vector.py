from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("2deep_output.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        text = row["ExtractedText"]
    
        if pd.isna(text) or not isinstance(text, str) or text.strip() == "":
            print(f"Skipping row {i}: invalid page_content")
            continue

        document = Document(
            page_content=text,
            metadata={"URL": row["URL"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

        
vector_store = Chroma(
    collection_name="UVA_websites",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)