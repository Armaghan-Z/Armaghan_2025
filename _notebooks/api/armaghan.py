from flask import Flask, jsonify
from flask_cors import CORS

# initialize a flask application (app)
app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')  # Allow all origins (*)

# ... your existing Flask

# add an api endpoint to flask app
@app.route('/api/armaghan')
def get_data():
    # start a list, to be used like a information database
    InfoDb = []

    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Armaghan",
        "LastName": "Zarak",
        "DOB": "October 21",
        "Residence": "San Diego",
        "Email": "Armaghanz@icloud.com",
        "Owns_Vehicles": ["2015-scooter", "Half-a-bike", "2013-Honda-Pilot", "The-other-half-of-the-bike"]
    })

    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Bob",
        "LastName": "Joe",
        "DOB": "July 4",
        "Residence": "The Atlantic Ocean",
        "Email": "bobjoe@powayusd.com",
        "Owns_Vehicles": ["Left-foot", "Half-a-right-foot"]
    })
    
    return jsonify(InfoDb)


# add an HTML endpoint to flask app
@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Hellox</title>
    </head>
    <body>
        <h2>Hello, mr bob!</h2>
    </body>
    </html>
    
    """
    
    return html_content

if __name__ == '__main__':
    # starts flask server on default port, http://127.0.0.1:5001
    app.run(port=5001)