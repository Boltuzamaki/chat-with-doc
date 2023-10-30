from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader


def document_laoder(doc_name, chunk_size=300, chunk_overlap=20, doc_type="pdf"):
    if doc_type == "pdf":
        loader = PyPDFLoader(doc_name)
        pages = loader.load_and_split()
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        docs = text_splitter.split_documents(pages)
        return docs
