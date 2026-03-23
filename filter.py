from flask import Flask , render_template , redirect , url_for




app = Flask(__name__,template_folder='templates')

@app.route("/")
def index():
    my_list =[10,20,30,40]
    
    return render_template('index.html',my_list=my_list)

@app.route("/filter")
def filter_page():
    
    some_text ='Hello'
    
    return render_template('filter.html', some_text=some_text)

@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for('filter_page'))



# Create my how filter
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]




if __name__=='__main__':
    app.run(debug=True)