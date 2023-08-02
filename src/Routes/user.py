from flask import request,jsonify
from src.Controllers.userController import postUserController,getUserController,getUserPasswordSecurityController,getUserAllController,putUserController
def userRoute (app):
    @app.route('/users', methods = [ 'POST', 'GET','PUT'])
    def user():
        if request.method == 'GET':
            if 'securityResponse' in request.args:
                code = request.args.get('code')
                securityResponse = request.args.get('securityResponse')
                response = getUserPasswordSecurityController(code,securityResponse)
                return jsonify(
                        response = response
                    )
            elif 'password' in request.args:
                code = request.args.get('code')
                password = request.args.get('password')
                response = getUserController(code,password)
                return jsonify(
                        response = response
                    )
            else:
                response = getUserAllController()
                return jsonify(
                        response = response
                    )
        if request.method == 'POST':
            code = request.form.get('code')
            password = request.form.get('password')
            idProfile = request.form.get('idProfile')
            response = postUserController(code,password,idProfile)
            return jsonify(
                response = response
            )
        if request.method == 'PUT':
            idUser = request.form.get('idUser')
            idRole = request.form.get('idRole')
            response = putUserController(idUser,idRole)
            return jsonify(
                response = response
            )