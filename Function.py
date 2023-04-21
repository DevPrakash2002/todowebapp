def open_todos():
    """
    Read a text file and return the list of
    to-do items
    """
    with open('todos.txt', 'r') as file_new:
        todos_new = file_new.readlines()
    return todos_new


def write_todos(todos_arg):
    with open('todos.txt', 'w') as fil:
        fil.writelines(todos_arg)