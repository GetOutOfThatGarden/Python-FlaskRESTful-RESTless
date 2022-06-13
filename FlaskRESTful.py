# Using flask to make an API
# This is the first thing I'm doing with python, alongside the other code in this folder (FlaskRESTless.py). My python is at beginner level as I follow this code.
# I'm following this tutorial: https://chukslord.hashnode.dev/writing-apis-with-python-the-flask-restful-way-1

# The following code is for the flaskRESTLfull way from the tutorial.

# Note that any comments starting with two #s are from the tutorial. Single #s are my own comments.

from flask import Flask
# These are the libraries being imported. I don't know what they mean yet, but I'll take a guess:
# 'reqparse' is for requiring an argument to be parsed.
# 'abort' is to abort a request
# 'API' is some thing got to do with the API.
# 'Resourse', I've no idea what this is yet.
from flask_restful import reqparse, abort, Api, Resource

#  I don't know why there is underscores on either side of 'name'. Is this a standard naming convention in py?
app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'sleep'},
    'todo2': {'task': 'eat'},
    'todo3': {'task': 'code!'},
    'todo4': {'task': 'repeat'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task')

# displays a single todo item and lets you delete a todo item
# What is the 'resource' entered as an argument into the function?


class Todo(Resource):
    # What is the 'self' for?
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return 'You have deleted the todo item', 204

    # Seems to be defining the route for the PUT request.
    def put(self, todo_id):
        # I need to figure out what
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return TODOS

    # Still not sure what 'self' is.
    def post(self):
        args = parser.parse_args()
        # Here we are creating a new todo item I think. But I still don't know what the methods are (max(), .keys(), .lstrip())
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        # Ok I figured out what the %i is, it is a placeholder that will be replaced with what comes after the second %. But what is the 'i' for? I learned what %s and %d is, but not %i yet.
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

# Setup the api resource routing here
# The author wrote the original comment above. Maybe this is associated with the 'resource' import from above.


# Is the below line creating a list?
api.add_resource(TodoList, '/todos')
# And maybe the below line is creating a single todo item?
api.add_resource(Todo, '/todos/<todo_id>')

# Again, just like the code from the RESTless tutorial, I've no idea what this is for. Is it the code to make the program run? What does 'debug=true' mean?
if __name__ == '__main__':
    app.run(debug=True)
