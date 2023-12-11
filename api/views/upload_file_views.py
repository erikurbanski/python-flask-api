from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
import os
import uuid

class UploadFileList(Resource):
    def post(self):
        file = request.files['file']
        if file.filename is None:
            return make_response(jsonify(message="Nenhum arquivo informado"), 500)
        
        filename = str(uuid.uuid4())
        file.save(os.path.join("uploads", filename))

        return make_response(jsonify(message="Upload realizado com sucesso"), 201)


api.add_resource(UploadFileList, '/upload-files')
