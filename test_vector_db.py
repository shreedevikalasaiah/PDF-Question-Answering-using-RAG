from loaders.pdf_loader import PDFLoader
from services.vector_db import VectorDB

docs = PDFLoader.load_pdf(r"C:\Users\A1\RAG project\data\shree resume.pdf")

db = VectorDB.create(docs)

print("Database Created Successfully")