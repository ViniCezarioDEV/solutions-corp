from flask import Flask, render_template, request, send_from_directory
from waitress import serve #SERVER
import Ariel
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'solutions-corp/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/projetos")
def projetos():
    return render_template('projetos.html')

@app.route("/ariel", methods=['GET', 'POST'])
def ariel():
    downloaded_files = []
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            user_input = request.form.get('user_input')
            Ariel.LIST_MUSICS.append(user_input)
        elif action == 'clear':
            Ariel.LIST_MUSICS.clear()
        elif action == 'download':
            downloaded_files = Ariel.YTdownloader()
    return render_template('ariel.html', lista=Ariel.LIST_MUSICS, status=Ariel.STATUS_LIST, files=downloaded_files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000) #SERVER
    #app.run(debug=True)
