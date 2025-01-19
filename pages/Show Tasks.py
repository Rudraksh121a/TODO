import streamlit as st

st.write("### ALL Tasks")
with open(r'Database/task.txt','r') as f:
    tasks=f.readlines()
    for task in tasks:
        st.text(task.strip())



