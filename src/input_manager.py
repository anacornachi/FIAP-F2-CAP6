from src.schemas.input_schema import input_schema
from src.validations import prompt_and_validate, validate_with_schema
from src.files import save_data, load_json_list
from src.files import load_data

INPUT_FILE = "data/insumos.json"

def register_input():
    print("\n💧 Cadastro de Insumo Agrícola")
    fields = ["crop_name", "input_type", "input_name", "quantity", "unit", "application_date"]

    validated_data = prompt_and_validate(input_schema, fields)
    if validated_data:
        save_data(INPUT_FILE, validated_data)
        print("✅ Insumo cadastrado com sucesso!\n")

def import_inputs_from_json():
    print("\n📂 Importação de Insumos via JSON")
    path = input("Informe o caminho do arquivo: ").strip()
    data = load_json_list(path)

    if not data:
        print("⚠️ Nenhum dado válido encontrado.")
        return

    success, failure = 0, 0
    for i, item in enumerate(data, start=1):
        is_valid, result = validate_with_schema(input_schema, item)
        if is_valid:
            save_data(INPUT_FILE, result)
            success += 1
        else:
            print(f"\n❌ Erros no registro {i}:")
            for field, msgs in result.items():
                for msg in msgs:
                    print(f" - {field}: {msg}")
            failure += 1

    print(f"\n✅ {success} insumo(s) importado(s) com sucesso. ❌ {failure} com erro(s).")
