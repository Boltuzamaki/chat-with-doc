from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
from prompt_templates import RAG_QA_TEMPLATE

load_dotenv()


def response_generator(question, docsearch):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=os.environ["PINECONE_API_KEY"],
    )
    template_prompt = PromptTemplate(
        template=RAG_QA_TEMPLATE, input_variables=["question", "context"]
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=docsearch.as_retriever(),
        chain_type_kwargs={"prompt": template_prompt},
    )
    result = qa_chain({"query": question})
    return result["result"]
