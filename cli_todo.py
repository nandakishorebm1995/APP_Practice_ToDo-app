# from main_functions import get_todos, write_todo_file
import main_functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)

"""
This project allows the user to add, show, edit and complete
To-Do list items. 
"""

# Keep the loop running until exit option is selected
while True:
    user_action = input('Type add, show, edit, complete, finish or exit: ')
    user_action = user_action.lower()
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        todo2 = todo + '\n'
        todos = main_functions.get_todos()
        todos.append(todo2.lower())
        main_functions.write_todo_file(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = main_functions.get_todos()
        if len(todos) == 0:
            print('Your To-Do list is empty. Please add to show them.')
        else:
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                index_n = index + 1
                print(f'{index_n}. {item}')

    elif user_action.startswith('edit'):
        todos = main_functions.get_todos()
        if len(todos) == 0:
            print('Your To-Do list is empty. Please add to edit them.')
        elif any(map(str.isdigit, user_action)):
            try:
                toEdit = int(user_action[5:]) - 1
                todoEdit = input('Edit your todo:') + '\n'
                todos[toEdit] = todoEdit.lower()
                main_functions.write_todo_file(todos)
            except IndexError:
                print("Oops! Your number exceeds the maximum. Try again...")
            except ValueError:
                print('Please enter a valid number:')
                continue
        else:
            try:
                user_action_act = user_action[5:] + '\n'
                toEdit_index = todos.index(user_action_act)
                todoEdit = input('Edit your todo:') + '\n'
                todos[toEdit_index] = todoEdit.lower()
                main_functions.write_todo_file(todos)
            except ValueError:
                print('Please type the correct todo item...')
                continue

    elif user_action.startswith('complete'):
        todos = main_functions.get_todos()
        try:
            if len(todos) == 0:
                print('Your To-Do list is already empty.')
            else:
                completed = int(user_action[9:]) - 1
                todos.pop(completed)
                main_functions.write_todo_file(todos)
        except ValueError:
            print('Please input the To-Do number also e.g. \"complete 5\"')

    elif user_action.startswith('finish'):
        todos = main_functions.get_todos()
        if len(todos) == 0:
            print('Your To-Do list is already empty.')
        else:
            confirm = input('Are you sure of deleting all your todos? If so, type \"yes\" else type \"no\": ')
            confirm = confirm.strip()
            confirm = confirm.capitalize()
            if confirm.startswith('y'):
                todos.clear()
                main_functions.write_todo_file(todos)
                print('Your To-Do list is cleared...')

    elif user_action.startswith('exit'):
        break
    else:
        print('Please select a valid action...')

print('Bye!')
