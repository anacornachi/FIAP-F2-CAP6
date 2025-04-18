from src.repositories.crop import get_all_crops
from src.repositories.input import get_applications_by_crop_id, get_applications_by_input_id, get_all_inputs


def generate_crop_report():
    print("\n📋 Relatório de Culturas Registradas\n")

    try:
        cultures = get_all_crops()
    except Exception as e:
        print(f"❌ Erro ao buscar culturas no banco: {e}")
        return

    if not cultures:
        print("⚠️ Nenhuma cultura cadastrada.")
        return

    for crop in cultures:
        print(f"🌱 Cultura: {crop['name']}")
        print(f"  📅 Plantio: {crop['planting_date'].strftime('%Y-%m-%d')}")
        print(f"  🌾 Colheita: {crop['harvest_date'].strftime('%Y-%m-%d') if crop['harvest_date'] else 'Não colhida'}")
        print(f"  📐 Área: {crop['area']} ha")
        print(f"  📊 Produtividade estimada: {crop['productivity']} toneladas")

        try:
            applications = get_applications_by_crop_id(crop["id"])
        except Exception as e:
            print(f"  ⚠️ Erro ao buscar insumos aplicados: {e}")
            continue

        if not applications:
            print("  🧪 Insumos aplicados: Nenhum")
        else:
            print("  🧪 Insumos aplicados:")
            for app in applications:
                print(f"    - {app['input_name']} ({app['input_type']}): {app['quantity']} {app['unit']} em {app['application_date'].strftime('%Y-%m-%d')}")

        print("-" * 50)



def generate_input_report():
    print("\n📦 Relatório de Insumos Registrados\n")

    try:
        inputs = get_all_inputs()
    except Exception as e:
        print(f"❌ Erro ao buscar insumos no banco: {e}")
        return

    if not inputs:
        print("⚠️ Nenhum insumo cadastrado.")
        return

    for insumo in inputs:
        print(f"🧪 Insumo: {insumo['input_name']}")
        print(f"  🧾 Tipo: {insumo['input_type']}")
        print(f"  📐 Unidade: {insumo['unit']}")
        print(f"  💰 Preço unitário: R$ {insumo['unit_price']:.2f}")

        try:
            apps = get_applications_by_input_id(insumo["id"])
        except Exception as e:
            print(f"  ⚠️ Erro ao buscar aplicações: {e}")
            continue

        if not apps:
            print("  🚫 Não aplicado em nenhuma cultura.")
        else:
            total_aplicado = sum([app["quantity"] for app in apps])
            print(f"  ✅ Total aplicado: {total_aplicado} {insumo['unit']}")
            print("  🌱 Aplicado nas culturas:")
            for app in apps:
                print(f"    - {app['crop_name']} em {app['application_date'].strftime('%Y-%m-%d')}")

        print("-" * 50)
