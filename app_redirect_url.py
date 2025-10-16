from flask import Flask, render_template, url_for, redirect

# app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', myList=[1, 2, 3, 4, 5])

@app.route('/other')
def other():
    some_text = "Hi Nini"
    return render_template('other.html', some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    app.run(debug=True)