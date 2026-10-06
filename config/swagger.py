get_all_spec = {
    "responses": {
        "200": {
            "description": "Lista de Consoles retornada com sucesso",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "nome": {"type": "string"},
                        "ano": {"type": "integer"},
                        "empresa": {"type": "string"},
                        "historia": {"type": "string"}
                    }
                }
            }
        }
    }
}

get_by_id_spec = {
    "parameters": [
        {
            "name": "console_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do console"
        }
    ],
    "responses": {
        "200": {"description": "Console encontrado com sucesso"},
        "404": {"description": "Console não encontrada"}
    }
}

get_by_ano_spec = {
    "parameters": [
        {
            "name": "ano",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Ano de lançamento do console"
        }
    ],
    "responses": {
        "200": {
            "description": "Lista de consoles do ano retornada com sucesso",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "nome": {"type": "string"},
                        "ano": {"type": "integer"},
                        "empresa": {"type": "string"},
                        "historia": {"type": "string"}
                    }
                }
            }
        },
        "404": {"description": "Nenhum console encontrado para este ano"}
    }
}

get_by_empresa_spec = {
    "parameters": [
        {
            "name": "empresa",
            "in": "path",
            "type": "string",
            "required": True,
            "description": "Nome da empresa fabricante do console"
        }
    ],
    "responses": {
        "200": {
            "description": "Lista de consoles da empresa retornada com sucesso",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "nome": {"type": "string"},
                        "ano": {"type": "integer"},
                        "empresa": {"type": "string"},
                        "historia": {"type": "string"}
                    }
                }
            }
        },
        "404": {"description": "Nenhum console encontrado para esta empresa"}
    }
}


insert_spec = {
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "ano": {"type": "integer"},
                    "empresa": {"type": "string"},
                    "historia": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        "201": {"description": "console cadastrado com sucesso"}
    }
}

update_spec = {
    "parameters": [
        {
            "name": "console_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do Console"
        },
       {
            "name": "body",
            "in": "body",
            "required": True,           
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "ano": {"type": "integer"},
                    "empresa": {"type": "string"},
                    "historia": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        "200": {"description": "Console atualizado com sucesso"},
        "404": {"description": "Console não encontrado"}
    }
}

delete_spec = {
    "parameters": [
        {
            "name": "console_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do console"
        }
    ],
    "responses": {
        "200": {"description": "console removido com sucesso"},
        "404": {"description": "console não encontrado"}
    }
}
