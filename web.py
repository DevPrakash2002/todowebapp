import streamlit as st
import Function

def add_todo():

    todo = '\n' + st.session_state["new_todo"]
    todos.append(todo)
    Function.write_todos(todos)


todos = Function.open_todos()
st.title(' MY TODO APP ')


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='',placeholder="Add New Todo From Here",
              on_change=add_todo, key= 'new_todo')
