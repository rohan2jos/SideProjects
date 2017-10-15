from flask import Flask, jsonify, abort
from flask_pymongo import PyMongo

# setup the app
app = Flask(__name__)
app.debug = True

# setup the tasks so that it can then be returned
# this is actually supposed to go into a database
tasks = [
    {
        "id": 1,
        "name": u'Groceries',
        "description": u'Buy milk, buy cheese, buy chicken',
        "Completed": False
    },
    {
        "id": 2,
        "name": u'complete insurance',
        "description": u'Check the mail and complete the insurance papers',
        "Completed": False
    },
    {
        "id": 3,
        "name": u'complete API',
        "description": u'Complete the python api, and then integrate database access',
        "Completed": False
    }]


# setup the index route
@app.route('/')
def index():
    return "hello world!"

# setup a route to get the request
@app.route('/api/todo/tasks', methods=['GET'])
def get_tasks():
    print "user is trying to get the tasks"
    return jsonify({'tasks': tasks})

# setup a route to extract a particular request
@app.route('/api/todo/tasks/<int:task_id>', methods=['GET'])
def get_a_task(task_id):
    print "the user wants to get a specific task"
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        print "does not match, requested unknown task"
        return "Please check the task number"
        abort(404)
    else:
        return jsonify({'task': task[0]})

# collect the details and then run the app
if __name__ == '__main__':
    app.run()