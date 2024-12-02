from flask import Flask, render_template, request
from waitress import serve #SERVER

app = Flask(__name__)

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

if __name__ == "__main__":
    #serve(app, host='0.0.0.0', port=5000) #SERVER
    app.run(debug=True)