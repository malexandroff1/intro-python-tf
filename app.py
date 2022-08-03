import os
from flask import Flask
from flask import request
from werkzeug.utils import secure_filename

from utils import procesar_archivo

UPLOAD_FOLDER = "/archivos"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_PATH"] = 2048


personas = []


@app.route("/subir-archivo", methods=["POST"])
def subir_archivo():
    try:
        archivo = request.files["archivo"]
        archivo = secure_filename(archivo.filename)
        archivo.save(os.path.join(app.config["UPLOAD_FOLDER"], archivo))
        personas = procesar_archivo(archivo.filename)
    except KeyError:
        return dict(mensaje="Error: archivo csv es requerido"), 400
    return dict(mensaje="archivo subido correctamente"), 200
