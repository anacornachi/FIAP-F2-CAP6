from src import crop_manager, forecast, reports, input_manager


def show_menu():
    print("\n=== Sistema de Gestão Agrícola ===")
    print("1. Cadastrar cultura manualmente")
    print("2. Importar culturas via JSON")
    print("3. Cadastrar insumo manualmente")
    print("4. Importar insumos via JSON")
    print("5. Aplicar insumo em cultura")
    print("6. Relatório de culturas")
    print("7. Relatório de insumos")
    print("8. Prever demanda de insumo")
    print("9. Atualizar data de colheita")
    print("10. Sair")


def main():
    while True:
        show_menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            crop_manager.register_crop()
        elif option == "2":
            crop_manager.import_crops_from_json()
        elif option == "3":
            input_manager.register_input()
        elif option == "4":
            input_manager.import_inputs_from_json()
        elif option == "5":
            input_manager.apply_input_to_crop()
        elif option == "6":
            reports.generate_crop_report()
        elif option == "7":
            reports.generate_input_report()
        elif option == "8":
            forecast.predict_demand()
        elif option == "9":
            crop_manager.update_harvest_date()
        elif option == "10":
            print("Encerrando o programa.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    print(f"📦 Versão do sistema: 0.4.0")
    main()

# TODO: Corrigir os testes
# TODO: Revisar documentação
# TOOD: Revisar entregável do projeto
