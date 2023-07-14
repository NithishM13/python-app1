import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="ib")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todos(),
                      key="lb",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15))
while True:
    event, value = window.read()
    # print(event)
    # print(value)
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = value['ib'] + "\n"

            todos.append(new_todo)
            functions.write_todos(todos)
            window['lb'].update(values=todos)
        case "Edit":
            todo_to_edit = value['lb'][0]
            new_todo = value['ib']

            todos = functions.read_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['lb'].update(values=todos)
        case "lb":
            window['ib'].update(value=value['lb'][0])
        case sg.WIN_CLOSED:
            break

window.close()
