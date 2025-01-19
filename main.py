import streamlit as st

# Streamlit Page Configuration
st.set_page_config(page_title="Task Management App", page_icon="📝", layout="centered")

# Title
st.title("Task Management App")

# Feature List
st.markdown("""
### Welcome to the Task Management App! 📝

This app allows you to manage your tasks efficiently. Here are the key features:

- **Add Tasks**: Easily add new tasks to your to-do list.
- **Modify Tasks**: Update the name of existing tasks.
- **View All Tasks**: View all the tasks you have added.
- **Delete Tasks**: Remove tasks you no longer need.
- **Persistent Storage**: Your tasks are saved in a text file for future access.

### How to Use:
1. **Add a new task** by entering the task name in the input box and clicking 'Add Task'.
2. **Modify existing tasks** by entering the task you want to modify and the new name for the task.
3. **View all tasks** to see your current list of tasks.
4. **Delete a task** by entering the name of the task you want to delete.

Start managing your tasks now by adding them to the list! 🎯
""")

# Your app's functionality code follows below...
