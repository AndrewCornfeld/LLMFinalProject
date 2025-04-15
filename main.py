from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about UVA. Only use the information from the provided sources below. Do not use any external or prior knowledge.

Here are some relevant websites: {websites}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print ("\n\n-----------------------------")
    question = input("What can I tell you about UVA today? (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    websites = retriever.invoke(question)
    print("retriever output")
    print(websites)
    websites_text = "\n\n".join([
        f"Source [{i+1}] ({doc.metadata.get('URL', 'No URL')}):\n{doc.page_content}"
        for i, doc in enumerate(websites)
    ])
    
    print("=== Prompt Sent to LLM ===")
    print(websites_text)

    # Run the chain
    result = chain.invoke({"websites": websites_text, "question": question})

    # Print the answer
    print("Answer:\n", result)

    # Print the source URLs
    print("\nSources:")
    for i, doc in enumerate(websites):
        print(f"[{i+1}] {doc.metadata.get('URL', 'No URL found')}")
