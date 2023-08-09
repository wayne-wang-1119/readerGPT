from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_key


pdf_path = "./paper.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(pages, embedding=embeddings, persist_directory=".")
vectordb.persist()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
pdf_qa = ConversationalRetrievalChain.from_llm(
    OpenAI(temperature=0.3), vectordb.as_retriever(), memory=memory
)


def main():
    with open("./question.txt", "r") as file:
        query = file.read()
    result = pdf_qa({"question": query})
    print("Answer:")
    result["answer"]


if __name__ == "__main__":
    main()
