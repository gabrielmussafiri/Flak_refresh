from flask import Flask , render_template , session , make_response , flash, request , redirect
app = Flask(__name__,template_folder='templates',static_folder='static', static_url_path='/')
app.secret_key='SOME KEY'


@app.route('/')
def index():
    return render_template('index.html',message='Index')

@app.route('/set_data')
def set_data():
    session['name'] ='Gabriel'
    session['surname']='Mussafiri'
    return render_template('index.html',message='Session data set')

@app.route('/get_dta')
def get_data():
    if "name" in session and 'surname' in session:
        name = session.get('name')
        surname = session.get('surname')
        return render_template('index.html',message =f'Name :{name} Surname: {surname}')
    else:
        return render_template('index.html',message ='No session found')
    
@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html',message ='Session clear')

@app.route('/set_cookies')
def set_cookies():
    response = make_response(render_template('index.html',message='Cookies Set'))
    response.set_cookie('cookie_name','cokkie_value')
    return response

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'gabriel' and password == 'admin123':
            flash('Sussessful Login!')
            return render_template('index.html',message ='')
        else:
            flash('Login Failed!')
            return redirect('login.html',message ='')
            


if __name__=='__main__':
    app.run(debug=True)