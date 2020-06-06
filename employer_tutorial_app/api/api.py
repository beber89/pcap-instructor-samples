import flask
from flask import request, jsonify, Response, make_response
from flask_cors import CORS, cross_origin
import json


app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

employees = []


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/employees', methods=['GET'])
def api_all():
    return jsonify(employees)

@app.route('/api/employee', methods=['POST'])
def add_employee():
    # EXERCISE: Create method converts json to Employee Object
    print(request.get_json())
    e = request.get_json()
    employees.append({'name': e['name'],\
        'age': e['age'],\
        'address': e['address']})
    print(employees)
    response = Response(mimetype="application/json",\
            status=201)
    return make_response(jsonify({"message": "OK"}), 200)
@app.route('/api/employee/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    # EXERCISE: Create method converts json to Employee Object
    return jsonify(employees[int(employee_id)])

app.run(host="0.0.0.0")