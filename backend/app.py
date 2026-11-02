from flask import Flask, jsonify
from connections import coll

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello from the backend!"})



@app.route('/api/get', methods=['GET'])
def api():
    names = coll.find()
    result =[]
    for name in names: 
        del name['_id']
        result.append(name['value'])
    result = {
        "data": result
    }
    names = list(names)    
    
    return jsonify(result)



@app.route("/api/add/<name>")
def add_name(name):
    coll.insert_one({"value": name})
    return jsonify({"message": f"Name '{name}' added successfully."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)