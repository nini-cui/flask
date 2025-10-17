from flask import Flask, render_template, session

app = Flask(__name__, template_folder='templates')
app.secret_key = "SOME KEY"

@app.route('/')
def index():
    return render_template('index_session.html', message='Index')

@app.route('/set_data')
def set_data():
    session['name'] = 'Nini'
    session['greeting'] = 'Hi'
    return render_template('index_session.html', message='Session data set')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'greeting' in session.keys():
        name = session['name']
        greeting = session['greeting']
        return render_template('index_session.html', message=f'Name: {name}, greeting: {greeting}')
    else:
        return render_template('index_session.html', message=f'No session found')
    
@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index_session.html', message=f'Session cleared')

if __name__ == '__main__':
    app.run(debug=True)