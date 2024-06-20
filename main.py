from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
import pymysql
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from fe_shorts_array import few_shots

from dotenv import load_dotenv
load_dotenv()
import os

def get_few_short_db_chain():
    llm=GoogleGenerativeAI(model="models/text-bison-001",google_api_key=os.environ["GOOGLE_PALM_API_KEY"], temperature=0.2)

    db_user="root"
    db_password="YK2002.yk"
    db_host="localhost"
    db_name="atliq_tshirts"

    db=SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

    hf_embed=HuggingFaceBgeEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-V2')

    to_be_vecorized=[" ".join(example.values()) for example in few_shots]

    vect_store=Chroma.from_texts(to_be_vecorized,embedding=hf_embed, metadatas=few_shots)

    sem_selecter=SemanticSimilarityExampleSelector(vectorstore=vect_store,k=2)

    example_prompt=PromptTemplate(
    input_variables=["Question","SQL Query","SQL Result","Answer"],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_srt_prmt=FewShotPromptTemplate(
        example_selector=sem_selecter,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input","table_info","top_k"]
    )

    new_db_chain=SQLDatabaseChain.from_llm(llm, db,verbose=True,prompt=few_srt_prmt)

    return new_db_chain
