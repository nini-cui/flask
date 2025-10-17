import pandas as pd
import os, uuid
from flask import Flask, render_template, request, Response, send_from_directory, jsonify

# app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index_post.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'Nini' and password == 'hi':
            return 'Success'
        else:
            return 'Failure'
        
@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type in ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel"):
        df = pd.read_excel(file)
        return df.to_html()
    
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']

    df = pd.read_excel(file)

    resp = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )
    return resp

@app.route('/convert_download_csv', methods=['POST'])
def convert_download_csv():
    file = request.files['file']

    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    file_name = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', file_name))

    return render_template('download.html', filename=file_name)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')

@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')

    return jsonify({'message': 'Successfully written!'})

if __name__ == '__main__':
    app.run(debug=True)