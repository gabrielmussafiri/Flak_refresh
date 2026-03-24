from flask import Flask , render_template , session
app = Flask(__name__,template_folder='templates',static_folder='static', static_url_path='/')
app.secret_key='SOME KEY'


@app.route('/')
def index():
    return render_template('index.html',message='Index')

@app.route('/set_data')
def set_data():
    session['name'] ='Gabriel'
    session['other']='Hello word'
    
    return render_template('index.html',message='Session data set')

@app.route('/get_dta')
def get_data

if __name__=='__main__':
    app.run(debug=True)