from src.schemas.crop_schema import crop_schema
from src.validations import prompt_and_validate, validate_with_schema
from src.files import save_data, load_json_list, load_data

CROPS_FILE = "data/culturas.json"

def register_crop():
    print("\n🌱 Cadastro de Cultura Agrícola")
    fields = ["name", "planting_date", "harvest_date", "area", "productivity"]

    validated_data = prompt_and_validate(crop_schema, fields)
    if validated_data:
        save_data(CROPS_FILE, validated_data)
        print("✅ Cultura cadastrada com sucesso!\n")

def import_crops_from_json():
    print("\n📂 Importação de Culturas via JSON")
    path = input("Informe o caminho do arquivo: ").strip()
    data = load_json_list(path)

    if not data:
        print("⚠️ Nenhum dado válido encontrado.")
        return

    success, failure = 0, 0
    for i, item in enumerate(data, start=1):
        is_valid, result = validate_with_schema(crop_schema, item)
        if is_valid:
            save_data(CROPS_FILE, result)
            success += 1
        else:
            print(f"\n❌ Erros no registro {i}:")
            for field, msgs in result.items():
                for msg in msgs:
                    print(f" - {field}: {msg}")
            failure += 1

    print(f"\n✅ {success} cultura(s) importada(s) com sucesso. ❌ {failure} com erro(s).")

def update_harvest_date():
    print("\n🌾 Atualizar data de colheita")
    name = input("Nome da cultura: ").strip()
    crops = load_data(CROPS_FILE)
    updated = False

    for crop in crops:
        if crop["name"].lower() == name.lower():
            if crop.get("harvest_date"):
                print("⚠️ Esta cultura já possui data de colheita.")
            else:
                new_date = input("Nova data de colheita (AAAA-MM-DD): ").strip()
                crop["harvest_date"] = new_date
                is_valid, result = validate_with_schema(crop_schema, crop)
                if is_valid:
                    updated = True
                else:
                    print("❌ Data inválida. Atualização não realizada.")
                    return

    if updated:
        save_data(CROPS_FILE, crops, overwrite=True)
        print("✅ Data de colheita atualizada.")
    else:
        print("❌ Cultura não encontrada ou já atualizada.")
