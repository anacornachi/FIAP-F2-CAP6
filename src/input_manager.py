from src.schemas.input_schema import input_schema
from src.validations import prompt_and_validate
from src.repositories.input_repository import save_input_to_db
from src.repositories.input_repository import save_input_application_to_db
from src.schemas.application_schema import application_schema
from src.validations import prompt_and_validate
from src.repositories.crop_repository import get_all_crops
from src.repositories.input_repository import get_all_inputs

def register_input():
    print("\n🧪 Cadastro de Insumo (catálogo)")
    fields = ["input_type", "input_name", "unit", "unit_price"]

    validated_data = prompt_and_validate(input_schema, fields)

    if validated_data:
        save_input_to_db(validated_data)
        print("✅ Insumo cadastrado com sucesso no catálogo!\n")

        should_link = input("Deseja vincular este insumo a alguma cultura agora? (s/n): ").strip().lower()
        if should_link == "s":
            print("🔗 Em breve será redirecionado para o vínculo com cultura...")
            apply_input_to_crop()
        else:
            print("👍 Cadastro finalizado. Você pode vincular este insumo mais tarde.\n")


def apply_input_to_crop():
    print("\n🔗 Vincular insumo a cultura")

    crops = get_all_crops()
    inputs = get_all_inputs()

    if not crops or not inputs:
        print("⚠️ É necessário ter pelo menos uma cultura e um insumo cadastrados.")
        return

    print("\n🌱 Culturas disponíveis:")
    for c in crops:
        print(f"{c['id']}: {c['name']}")

    print("\n🧪 Insumos disponíveis:")
    for i in inputs:
        print(f"{i['id']}: {i['input_name']} ({i['input_type']})")

    fields = [
        "crop_id",
        "input_id",
        "quantity",
        "unit",
        "application_date",
        "recurrence",
        "recurrence_days"
    ]

    validated_data = prompt_and_validate(application_schema, fields)

    if validated_data:
        save_input_application_to_db(validated_data)
        print("✅ Insumo aplicado à cultura com sucesso!\n")
