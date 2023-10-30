from langchain.vectorstores import Pinecone
import pinecone
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])


def pinecone_init():
    pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment=os.environ["PINECONE_ENVIRONMENT"],
    )


def create_new_index(index_name):
    pinecone_init()
    index = pinecone.Index(index_name)


def remove_index(index_name):
    pinecone_init()
    pinecone.delete_index(index_name)


def upsert_document_lanchain(docs, embeddings, index_name):
    docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    return docsearch


def load_existing_index(index_name, docs, embeddings):
    docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    return docsearch


def retrive_similar_documents_from_vectorstore(query, docsearch, number_documents=3):
    docs = docsearch.similarity_search(query, k=number_documents)
    return docs
