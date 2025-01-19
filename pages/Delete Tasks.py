
import streamlit as st
all_tasks=[]
with open(r'Database/task.txt','r') as f:
    tasks=f.readlines()
    all_tasks=[task.strip() for task in tasks]

st.write("### All Task list")
for i in all_tasks:
    st.text(i)

delele_task=st.text_input("Enter the name of task")
if st.button("Delete"):
    if delele_task in all_tasks:
        all_tasks.remove(delele_task)

        with open(r'Database/task.txt','w') as f:
            for i in all_tasks:
                f.write(i+'\n')
        st.success(f'{delele_task} Delete Successfully')
    else:
        st.error(f"{delele_task} is not there ")
st.write("### Updated Task list")
for i in all_tasks:
    st.text(i)


