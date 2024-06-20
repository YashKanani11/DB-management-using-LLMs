from main import get_few_short_db_chain
import streamlit as st
st.title("DB management solutions by YASH")

question=st.text_input("Question:")

if question:
    chain=get_few_short_db_chain()
    ans=chain.run(question)
    st.header("Answer")
    st.write(ans)
