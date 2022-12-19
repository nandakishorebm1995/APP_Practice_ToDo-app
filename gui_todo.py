import main_functions
import PySimpleGUI as sg
import main_functions

label = sg.Text("Add your todo")
input_box = sg.InputText(tooltip="Enter todo", key="To-Do")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box], [add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    # event is the label of the button pushed
    # values are the input given by the user during that event.
    match event:
        case "Add":
            todos = main_functions.get_todos()
            todo = values["To-Do"] + '\n'
            todos.append(todo)
            print(todos)
            main_functions.write_todo_file(todos)

        case sg.WIN_CLOSED:
            break

window.close()

