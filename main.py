import os
from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI,OpenAIEmbeddings


class App:

    def __init__(self):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

        self._load_model()
        self._build_database()
        self._load_retriever()
        self._set_system_prompt()

    def _load_model(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0.1)

    def _load_retriever(self):
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 4})

    def _build_database(self):
        file_path = "data/seoul_data.csv"
        loader = CSVLoader(file_path=file_path, source_column="Name")
        docs = loader.load_and_split()

        embeddings = OpenAIEmbeddings()

        index = faiss.IndexFlatL2(len(embeddings.embed_query(" ")))
        self.vector_store = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={}
        )
        self.vector_store.add_documents(documents=docs)

    def _set_system_prompt(self):
        system_prompt = (
            """
            As a travel assistant, please utilize the retrieved documents to create a detailed travel itinerary for a user
             with specific constraints.
            For example:
            1. User: "I have a limited time of 4 hours in Seoul. Can you suggest a well-structured itinerary that
             includes must-see attractions and efficient transportation options?"
            2. User: "As a student with a budget of $15, could you recommend affordable attractions or activities
             in Seoul that I can visit, ensuring they are suitable for my budget and interests?"
            Please ensure your recommendations are polite, concise, and based solely on the information available in the documents. 
            Additionally, prioritize places based on their ratings or costs as specified in the documents.
            \n\n
            {context}
            """
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),

        ])

        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        self.rag_chain = create_retrieval_chain(self.retriever, question_answer_chain)

    def run_query(self, user_input: str) -> str:
        answer = self.rag_chain.invoke({"input": user_input})
        return answer['answer']
