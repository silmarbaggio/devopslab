
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Laboratorio DevOps - FIAP - SILMAR"

if __name__ == '__main__':
    app.run()