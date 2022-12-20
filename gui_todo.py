import main_functions
import PySimpleGUI as sg
import main_functions

label = sg.Text("Type in your To-Do:", font="Helvetica 13 bold")
input_box = sg.InputText(tooltip="Enter todo", key="To-Do")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=main_functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit", border_width=2, button_color="red", font="bold")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box], [edit_button, complete_button, sg.Push(), exit_button]],
                   font=("Helvetica", 13))

while True:
    event, values = window.read()
    # event is the label of the button pushed
    # values are the input given by the user during that event.
    match event:
        case "Add":
            todos = main_functions.get_todos()
            todo = values["To-Do"] + '\n'
            todos.append(todo)
            main_functions.write_todo_file(todos)
            window["todos"].update(values=todos)
            window["To-Do"].update(value=[])

        case "Edit":
            edit_todo = values["todos"][0]
            todos = main_functions.get_todos()
            edit_idx = todos.index(edit_todo)
            edited_todo = values["To-Do"]
            todos[edit_idx] = edited_todo
            main_functions.write_todo_file(todos)
            window["todos"].update(values=todos)
            window["To-Do"].update(value=[])

        case "Complete":
            todo_complete = values["todos"][0]
            todos = main_functions.get_todos()
            complete_idx = todos.index(todo_complete)
            todos.pop(complete_idx)
            main_functions.write_todo_file(todos)
            window["todos"].update(values=todos)
            window["To-Do"].update(value=[])

        case "Exit":
            break

        case "todos":
            window["To-Do"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()

