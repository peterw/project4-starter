import os
import openai
import streamlit as st
import shutil
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from streamlit_chat import message
from langchain.vectorstores import Pinecone
import pinecone