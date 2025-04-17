import unittest
from unittest.mock import patch, mock_open
import io
import sys
import json

from src.input_manager import register_input, import_inputs_from_json, apply_input_to_crop
from src.db.oracle import get_connection
from src.repositories.crop import get_all_crops
from src.repositories.input import get_all_inputs


class TestInputManagementE2E(unittest.TestCase):

    def setUp(self):
        # Limpa e prepara o banco antes de cada teste
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM crop_input_applications")
        cursor.execute("DELETE FROM inputs WHERE input_name IN ('NPK 4-14-8', 'Milho Híbrido')")
        cursor.execute("DELETE FROM crops WHERE name IN ('Milho', 'Soja')")
        cursor.execute("""
            INSERT INTO crops (name, planting_date, harvest_date, area, productivity)
            VALUES ('Milho', TO_DATE('2024-10-15', 'YYYY-MM-DD'), NULL, 5, 8)
        """)
        conn.commit()
        cursor.close()
        conn.close()

    @patch("builtins.input")
    def test_register_input_success(self, mock_input):
        mock_input.side_effect = ["fertilizante", "NPK 4-14-8", "kg", "4.5", "n"]
        captured = io.StringIO()
        sys.stdout = captured
        register_input()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("✅ Insumo cadastrado com sucesso", output)

    @patch("builtins.input", return_value="mock_insumos.json")
    @patch("src.input_manager.open", new_callable=mock_open, read_data=json.dumps([
        {"input_type": "fertilizante", "input_name": "NPK 4-14-8", "unit": "kg", "unit_price": 4.5},
        {"input_type": "semente", "input_name": "Milho Híbrido", "unit": "sacos", "unit_price": 300.0}
    ]))
    def test_import_inputs_success(self, mock_file, mock_input):
        captured = io.StringIO()
        sys.stdout = captured
        import_inputs_from_json()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("✅ 2 insumo(s) importado(s) com sucesso", output)

    @patch("builtins.input", return_value="mock_insumos.json")
    @patch("src.input_manager.open", new_callable=mock_open, read_data=json.dumps([
        {"input_type": "fertilizante", "input_name": "", "unit": "kg", "unit_price": 4.5}
    ]))
    def test_import_inputs_with_error(self, mock_file, mock_input):
        captured = io.StringIO()
        sys.stdout = captured
        import_inputs_from_json()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("❌ Erros no registro 1:", output)

    @patch("builtins.input")
    def test_apply_input_to_crop_success(self, mock_input):
        inputs = get_all_inputs()
        crops = get_all_crops()
        if not inputs or not crops:
            self.skipTest("Insumos e culturas devem estar cadastrados antes deste teste.")

        mock_input.side_effect = [
            str(crops[0]["id"]),               # crop_id
            str(inputs[0]["id"]),              # input_id
            "10",                              # quantity
            "2024-11-01",                      # application_date
            "semanal",                         # recurrence
            "7"                                # recurrence_days
        ]
        captured = io.StringIO()
        sys.stdout = captured
        apply_input_to_crop()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("✅ Insumo aplicado à cultura com sucesso", output)


if __name__ == "__main__":
    unittest.main()
