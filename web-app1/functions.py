FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH):
    """ Read the items in the given text-file
     and returs them as a list.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(lst, filepath=FILEPATH):
    """ Write the list in a given text-file."""
    with open(filepath, "w") as file:
        file.writelines(lst)

