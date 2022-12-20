import main_functions
import PySimpleGUI as sg
import main_functions

label = sg.Text("Type in your todo")
input_box = sg.InputText(tooltip="Enter todo", key="To-Do")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=main_functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")


window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 13))

while True:
    event, values = window.read()
    # event is the label of the button pushed
    # values are the input given by the user during that event.
    print(event)
    print(values)

    match event:
        case "Add":
            todos = main_functions.get_todos()
            todo = values["To-Do"] + '\n'
            todos.append(todo)
            main_functions.write_todo_file(todos)
            window["todos"].update(values=todos)
            window["To-Do"].update(value=[])

        case "Edit":
            print(values)
            edit_todo = values["todos"][0]
            todos = main_functions.get_todos()
            edit_idx = todos.index(edit_todo)
            edited_todo = values["To-Do"]
            todos[edit_idx] = edited_todo
            main_functions.write_todo_file(todos)
            window["todos"].update(values=todos)
            window["To-Do"].update(value=[])

        case "todos":
            window["To-Do"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()

