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
            "name": "cansole_id",
            "in": "path",
            "type": "intereger",
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
