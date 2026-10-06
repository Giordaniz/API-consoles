from flask import jsonify
from models.console import ConsoleModel

class ConsoleController:
    @staticmethod
    def mostrar_tudo():
        consoles = ConsoleModel.get_all()
        return jsonify(consoles)

    @staticmethod
    def mostrar_por_id(console_id):
        console = ConsoleModel.get_by_id(console_id)
        if console:
            return jsonify(console)
        return jsonify({"erro": "Console não encontrado"}), 404

    @staticmethod
    def mostrar_por_ano(ano):
        consoles = ConsoleModel.get_by_ano(ano)
        if consoles:
            return jsonify(consoles)
        return jsonify({"erro": "Nenhum console encontrado para este ano"}), 404

    @staticmethod
    def mostrar_por_empresa(empresa):
        consoles = ConsoleModel.get_by_empresa(empresa)
        if consoles:
            return jsonify(consoles)
        return jsonify({"erro": "Nenhum console encontrado para esta empresa"}), 404

    @staticmethod
    def cadastrar(dados):
        novo_id = ConsoleModel.insert (dados)
        return jsonify({"mensagem": "Console cadastrada com sucesso", "id": novo_id}), 201

    @staticmethod
    def atualizar(console_id, dados):
        sucesso = ConsoleModel.update(console_id, dados)
        if sucesso:
            return jsonify({"mensagem": "Console atualizado"})
        return jsonify({"erro": "Console não encontrado"}), 404
    
    @staticmethod
    def excluir(console_id):  
        sucesso = ConsoleModel.delete(console_id)  
        if sucesso:
            return jsonify({"mensagem": "Console excluído"})
        return jsonify({"erro": "Console não encontrado"}), 404
    