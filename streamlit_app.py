from main import get_few_short_db_chain
import streamlit as st
st.title("DB management solutions by YASH")

question=st.text_input("Question:")

if question:
    chain=get_few_short_db_chain()
    ans=chain.run(question)
    st.header("Answer")
    st.write(ans)

st.text_area("This is a representation of Levi's store, you can ask question abt sizes and price and any other complex query")
st.text_area("If you get any error please mail your query to 'ykkanani.yk@outlook.com' ")
