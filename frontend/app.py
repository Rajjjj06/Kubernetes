from flask import Flask, render_template
import os
import requests

app = Flask(__name__)
port = int(os.environ.get('PORT', 8080))
BACKEND_URL=os.environ.get('BACKEND_URL', 'http://localhost:5000')

@app.route('/')
def index():
    
    response = requests.get(f"{BACKEND_URL}/api/get")
    data = response.json()
    
    print(data, type(data))
    
    env = dict(os.environ)
    return render_template('index.html', env=env, data=data['data'])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)