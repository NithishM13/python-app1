import functions
import time

now = time.strftime("%b %d, %Y %H:%M")
print("Today is", now)

while True:

    user_action = input("What do you like to do, like 'add', 'edit', 'view', 'complete' or 'exit': ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.read_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("view"):
        todos = functions.read_todos()

        for index, items in enumerate(todos):
            items = items.strip("\n")
            print(f"{index + 1}. {items}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.read_todos()

            new_todo = input("Enter a new Todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your input is invalid. Please enter a number after edit command.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.read_todos()

            remove_todo = todos[number].strip("\n")
            todos.pop(number)

            functions.write_todos(todos)

            message = f"The todo({remove_todo}) has been removed from the List."
            print(message)

        except IndexError:
            print("Your input is invalid. Please enter the correct number of the todo to mark completed.")
            continue

    elif user_action.startswith("exit"):
        print("Noice meeting You!!!")
        break

    else:
        print("Please enter a valid command.")
