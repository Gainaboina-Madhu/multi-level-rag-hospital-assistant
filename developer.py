import numpy as np
import langchain
import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import dotenv
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_AI_KEY")

openai_embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")


for i in os.listdir("data"):
    d = TextLoader("./data/"+i)
    print(f'loading the data from file {d} : {i}')

    chunk_obj = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=150)
    individual_docs = chunk_obj.split_documents(d.load())
    print(f'The one Document is divide it into multiple chunks {len(individual_docs)}')

    chroma_db = Chroma.from_documents(individual_docs, openai_embedding_model, persist_directory='./db/'+i+' database')

    print(f'DB stored')







