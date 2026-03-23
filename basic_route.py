from flask import Flask , request , make_response



app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route("/hello")
def hello():
    response = make_response('Hello word')
    response.status_code = 202
    response.headers['content-type'] ='application/octet-stream'
    
    return response

# url frocessur
@app.route('/greet/<name>')
def greet(name):
    
    return f'hello {name}'

@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
    
    return f'{number1} +{number2} = {number1 + number2}'

@app.route('/params')
def params():
    if "greeting" in request.args.key() and 'name' in request.args.key():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        
        return f'{greeting},{name}'
    else :
        return ' Some params missing'
    
if __name__ == '__main__':
    app.run(debug=True)