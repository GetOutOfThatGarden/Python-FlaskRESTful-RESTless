# Using flask to make an API
# This is the first thing I'm doing with python, my python is at beginner level as I follow this code.
# I'm following this tutorial: https://chukslord.hashnode.dev/writing-apis-with-python-the-flask-restful-way-1

# The following code is for the flaskRESTLESSS way from the tutorial.

# import necessaty files and functions
from flask import Flask, jsonify, request

# create a flask app
# not sure what they mean by app here. Will this be called later in the code?
app = Flask(__name__)

# Below is the todo list from the guide. I guess is it some sort of array? Or is it creating a list of objects?
TODOS = {
    'todo1': {'task': 'sleep'},
    'todo2': {'task': 'eat'},
    'todo3': {'task': 'code'},
    'todo4': {'task': 'repeat'}
}
# I'm still confused about the struture of the above code. Are those four objects I just created?

# I don't know what 'def' is.
# Does it mean it is defining a function?
# Possibly, maybe it's called abort_if_todo_doesnt_exist with a argument of todo_id being passed into it.
# but todo_id has not been defined yet, will it show up later in the code?


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        message = "Todo {} doesn't exist".format(todo_id)
        # I'm guessing the below code uses a function called jsonify to create a json object.
        return jsonify({'message': message})

# @app.route('/todos/<todo_id>', methods=['GET','DELETE','PUT'])


def todo(todo_id):
    # I think the below code is if the api request was a GET request, as opposed to a PUT or DELETE request.
    if (request.method == 'GET'):
        abort_if_todo_doesnt_exist(todo_id)
        return jsonify({'data': TODOS[todo_id]})

    elif (request.method == 'DELETE'):
        abort_if_todo_doesnt_exist(todo_id)
        # I'm guessing the below code is deleting the todo from the TODOS list.
        del TODOS[todo_id]
        return jsonify({'message': 'You have deleted the todo item'}), 204

    elif (request.method == 'PUT'):
        abort_if_todo_doesnt_exist(todo_id)
       # Right now, I dont know what args is. Is it a variable?
       args = parser.parse_args()
       task = {'task': args['task']}
       TODOS[todo_id] = task
       return jsonify({'task':task}), 201

# @app.route('/todos', methods=['GET','POST'])
def todo_list():
    if (request.method == 'GET'):
        return jsonify({'data': TODOS})

    elif (request.method == 'POST'):
        args = parser.parse_args()
        #  Theres a few things in the below line that I don't understand. Like 'max', keys, and lstrip. I presume the '+ 1' at the end is incredmenting the number. Maybe this code is to give each new post a label of todo1, todo2, todo3, etc.
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        # Same with the below code. I dont know what the '%i' is. And why is there another % in the middle of the line? 
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return jsonify({'data': TODOS[todo_id]}), 201

# driver function
if __name__ == '__main__':
    # No idea what's going on here.
    app.run(debug=True)