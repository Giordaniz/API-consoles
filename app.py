from flask import Flask, request
from flasgger import Swagger, swag_from
from controllers.console_controller import ConsoleController
from config.swagger import (
get_all_spec,
get_by_id_spec, 
insert_spec, 
update_spec, 
delete_spec
)

app = Flask(__name__)

swagger_config = {
"headers": [],
"specs": [
{
"endpoint": 'apispec_1',
"route": '/apispec_1.json',
"rule_filter": lambda rule: True,
"model_filter": lambda rule: True,
}
],
"static_url_path": "/flasgger_static",
"swagger_ui": True,
"specs_route": "/consoles/swagger"
}

swagger = Swagger(app, config=swagger_config)

@app.route('/consoles', methods=['GET'])
@swag_from(get_all_spec)
def listar_todas():
    return ConsoleController.mostrar_tudo()

@app.route('/consoles/<int:console_id>', methods=['GET'])
@swag_from(get_by_id_spec)
def listar_por_id(console_id):
    return ConsoleController.mostrar_por_id(console_id)

@app.route('/console', methods=['POST'])
@swag_from(insert_spec)
def criar():
    dados = request.json
    return ConsoleController.cadastrar(dados)

@app.route('/console/<int:console_id>', methods=['PUT'])
@swag_from(update_spec)
def atualizar(console_id):
    dados = request.json
    return ConsoleController.atualizar(console_id, dados)

@app.route('/console/<int:console_id>', methods=['DELETE'])
@swag_from(delete_spec)
def deletar(console_id):
    return ConsoleController.excluir(console_id)

if __name__ == '__main__':
    app.run(debug=True)