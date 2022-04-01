from flask import Flask,jsonify
from flask import request,json
app = Flask(__name__)



todos =  [
    { "label": "My first task", "done": False }
    ]

@app.route('/blabla', methods=['GET'])
def hello_world():
    
    return '<h1>Hello!</h1>'

@app.route('/todos', methods=['GET'])
def Todos():
    
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    #curl -X POST 0.0.0.0:3245/todos -H "Content-Type: application/json" -d '{ "done": false, "label": "Sample Todo 3"}'
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)