from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from services.embeddings import EmbeddingModel
from config import DB_DIRECTORY
import os


class VectorDB:

    @staticmethod
    def create(documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(documents)

        db = Chroma.from_documents(
            documents=chunks,
            embedding=EmbeddingModel.load_embeddings(),
            persist_directory=DB_DIRECTORY
        )

        print("Vector Database Created Successfully")

        return db

    @staticmethod
    def load():

        print("=" * 60)
        print("Current Working Directory :", os.getcwd())
        print("Database Path :", os.path.abspath(DB_DIRECTORY))
        print("Database Exists :", os.path.exists(DB_DIRECTORY))
        print("=" * 60)

        embeddings = EmbeddingModel.load_embeddings()

        db = Chroma(
            persist_directory=DB_DIRECTORY,
            embedding_function=embeddings
        )

        print("Vector Database Loaded Successfully")

        return db