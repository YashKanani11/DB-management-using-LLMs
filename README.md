# DB Manager Using Gen AI & NLP

## Overview
This project is a sophisticated Retrieval-Augmented Generation (RAG) application called "DB Manager Using Gen AI & NLP." It leverages LangChain with Google's PaLM model to generate SQL queries by identifying specific table names, column names, and fields. The application also includes short learning mechanisms to handle complex queries and improve the model's performance over time.

## Features
1. Natural Language to SQL: Converts natural language queries into SQL queries using LangChain and Google's PaLM model.
2. Self-Learning: Implements short learning mechanisms to handle complex queries and improve the model's accuracy.
3. Embeddings and Vector Database: Uses Hugging Face embeddings to convert queries into vectors and stores them in ChromaDB.
4. Streamlit UI: Provides a simple and accessible user interface through Streamlit.
5. AWS RDS Integration: Connects to AWS RDS to upload and manage the database.

### Live Demo - [Live Demo @ streamlit](https://db-management-using-llms.streamlit.app "deployed on streamlit")

## Installation
1. Clone the repo
   
   git clone https://github.com/YashKanani11/DB-management-using-LLMs
   
   cd DB-management-using-LLMs

2. Create a virtual environment

   python3 -m venv venv
   
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies

   pip install -r requirements.txt
   
4. Google Palm API

   go to google ai website sign up/sign in

   create ur new api and copy the code(u wont be able to do it later, youll have to create a new api)
    
5. Configure AWS RDS

   go to aws - [AWS](https://aws.amazon.com/)

   sighn up / login

   go to rds section (search if u dont find)

   create a database instance make sure to make it publicaly accesible and after generating copy the endpoint

6. mysql Workbench

   download and setup workbench

   make a new connection and use the credentials u used to create aws database and in host paste the endpoint

   copy the database from this repo and run it

7. env setup

   create a .env file and add these specific values (keep the name same)
   
   a. GOOGLE_PALM_API_KEY="ur_api_key"
   
   b. AWS_RDS_ENDPOINT="ur_endpoint_.rds.amazonaws.com"
   
   c. AWS_RDS_PASSWORD="ur_pass"

8. Run the Application

   streamlit run streamlit_app.py
