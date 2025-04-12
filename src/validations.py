from copy import deepcopy
from cerberus import Validator

FRIENDLY_ERRORS = {
    "required field": "Campo obrigatório.",
    "empty values not allowed": "Este campo não pode ficar em branco.",
    "null value not allowed": "Este campo é obrigatório.",
    "value does not match regex": "Formato inválido. Use o formato AAAA-MM-DD.",
    "unallowed value": "Valor não permitido. Escolha uma das opções válidas.",
    "min value is": "Valor abaixo do mínimo permitido.",
    "must be of float type": "Digite um número com ponto decimal (ex: 2.5).",
    "must be of string type": "Digite um texto válido.",
}

FIELD_PROMPTS = {
    "name": "Nome da cultura: ",
    "planting_date": "Data do cultivo (AAAA-MM-DD): ",
    "harvest_date": "Data da colheita (caso ainda não tenha colhido, pressione Enter): ",
    "area": "Área plantada (em hectares): ",
    "productivity": "Produtividade estimada (em toneladas): ",
    "crop_name": "Nome da cultura associada ao insumo: ",
    "input_type": "Tipo de insumo (fertilizante, semente ou defensivo): ",
    "input_name": "Nome do insumo: ",
    "quantity": "Quantidade aplicada: ",
    "unit": "Unidade (kg, g, L, ml, sacos): ",
    "application_date": "Data de aplicação (AAAA-MM-DD): "
}

def translate_error(error: str) -> str:
    for key in FRIENDLY_ERRORS:
        if key in error:
            return FRIENDLY_ERRORS[key]
    return "Valor inválido. Tente novamente."


def validate_with_schema(schema: dict, data: dict) -> tuple:
    v = Validator(schema)
    if v.validate(data):
        return True, v.document
    else:
        return False, v.errors


def prompt_and_validate(schema: dict, fields_order: list) -> dict:
    result = {}

    for field in fields_order:
        original_schema = deepcopy(schema[field])
        field_schema = deepcopy(schema[field])
        field_schema["required"] = False

        validator = Validator({field: field_schema})
        label = FIELD_PROMPTS.get(field, f"{field.replace('_', ' ').capitalize()}: ")

        while True:
            value = input(label).strip()

            if schema[field]["type"] == "float":
                try:
                    value = float(value)
                except ValueError:
                    print("❌ Valor inválido. Digite um número com ponto decimal.")
                    continue

            if value == "":
                value = None

            if validator.validate({field: value}):
                if value is None and original_schema.get("nullable") is not True:
                    print("❌ Campo obrigatório.")
                    continue
                result[field] = value
                break
            else:
                print("❌", translate_error(str(validator.errors[field][0])))

    return result
