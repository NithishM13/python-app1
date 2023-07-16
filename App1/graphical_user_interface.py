import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple3")

clock = sg.Text('', key='Clock', text_color="orange")
label = sg.Text("Type in a To-Do", text_color="black")
input_box = sg.InputText(tooltip="Enter todo", key="ib")
add_button = sg.Button("Add", size=10, mouseover_colors="purple", pad=20, border_width=5)
list_box = sg.Listbox(values=functions.read_todos(),
                      key="lb",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit", mouseover_colors="purple", size=8, border_width=5)
complete_button = sg.Button("Complete", mouseover_colors="black", border_width=5)
exit_button = sg.Button("Exit",size=10, mouseover_colors="purple", pad=10, border_width=5)

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))
while True:
    event, value = window.read(timeout=300)
    window['Clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = value['ib'] + "\n"

            todos.append(new_todo)
            functions.write_todos(todos)
            window['lb'].update(values=todos)
            window['ib'].update(value='')
        case "Edit":
            try:
                todo_to_edit = value['lb'][0]
                new_todo = value['ib']

                todos = functions.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['lb'].update(values=todos)
            except IndexError:
                sg.popup("Please select a valid todo first.", title="Error", font=('Helvetica', 10))
        case "Complete":
            try:
                complete_todo = value['lb'][0]
                todos = functions.read_todos()
                todos.remove(complete_todo)
                functions.write_todos(todos)
                window['lb'].update(values=todos)
                window['ib'].update(value='')
            except IndexError:
                sg.popup("Please select a valid todo first.", title="Error", font=('Helvetica', 10))
        case "lb":
            window['ib'].update(value=value['lb'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
