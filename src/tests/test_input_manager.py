import warnings
warnings.filterwarnings("ignore")

import unittest
from unittest.mock import patch, mock_open
import io
import sys
import json
import os

from src.input_manager import register_input, import_inputs_from_json, apply_input_to_crop
from src.db.oracle import get_connection
from src.repositories.crop import get_all_crops
from src.repositories.input import get_all_inputs

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUTS_PATH = os.path.join(CURRENT_DIR, "../data/insumos.json")


class TestInputManagement(unittest.TestCase):

    def setUp(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM crop_input_applications")
        cursor.execute("DELETE FROM inputs WHERE input_name IN ('NPK 4-14-8', 'Milho Híbrido', 'Produto X')")
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
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            register_input()
            output = captured.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("✅ Insumo cadastrado com sucesso", output)

    @patch("builtins.input", return_value=INPUTS_PATH)
    @patch("src.input_manager.open", new_callable=mock_open, read_data=json.dumps([
        {"input_type": "fertilizante", "input_name": "NPK 4-14-8", "unit": "kg", "unit_price": 4.5},
        {"input_type": "semente", "input_name": "Milho Híbrido", "unit": "sacos", "unit_price": 300.0}
    ]))
    def test_import_inputs_success(self, mock_file, mock_input):
        captured = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            import_inputs_from_json()
            output = captured.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("✅ 2 insumo(s) importado(s) com sucesso", output)

    @patch("builtins.input", return_value=INPUTS_PATH)
    @patch("src.files.open", new_callable=mock_open, read_data=json.dumps([
        {"input_type": "fertilizante", "input_name": "", "unit": "kg", "unit_price": 4.5}
    ]))
    def test_import_inputs_with_error(self, mock_file, mock_input):
        captured = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            import_inputs_from_json()
            output = captured.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Erros no registro 1:", output)

    @patch("builtins.input")
    def test_apply_input_to_crop_success(self, mock_input):
        inputs = get_all_inputs()
        crops = get_all_crops()
        if not inputs or not crops:
            self.skipTest("Pré-condições não satisfeitas.")

        mock_input.side_effect = [
            str(crops[0]["id"]),
            str(inputs[0]["id"]),
            "10",
            "2024-11-01",
            "semanal",
            "7"
        ]

        captured = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            apply_input_to_crop()
            output = captured.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("✅ Insumo aplicado à cultura com sucesso", output)

    @patch("builtins.input")
    def test_register_input_missing_name(self, mock_input):
        mock_input.side_effect = [
            "fertilizante",
            "",
            "Produto X",
            "kg",
            "4.5",
            "n"
        ]

        captured = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            register_input()
            output = captured.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Este campo é obrigatório.", output)

    @patch("builtins.input")
    def test_register_input_invalid_unit(self, mock_input):
        mock_input.side_effect = ["fertilizante", "Produto X", "kilo", "kg", "4.5", "n"]

        captured = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            register_input()
            output = captured.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Valor não permitido. Escolha uma das opções válidas.", output)

    @patch("builtins.input")
    def test_register_input_invalid_price_format(self, mock_input):
        mock_input.side_effect = ["fertilizante", "Produto X", "kg", "abc", "4.5", "n"]

        captured = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            register_input()
            output = captured.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Valor inválido. Digite um número com ponto decimal.", output)

    @patch("builtins.input")
    def test_apply_input_with_invalid_date_then_correct(self, mock_input):
        inputs = get_all_inputs()
        crops = get_all_crops()
        if not inputs or not crops:
            self.skipTest("Pré-condições não satisfeitas.")

        mock_input.side_effect = [
            str(crops[0]["id"]),
            str(inputs[0]["id"]),
            "10",
            "31/12/2024",
            "2024-11-01",
            "mensal",
            "30"
        ]

        captured = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            apply_input_to_crop()
            output = captured.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Formato inválido. Use o formato AAAA-MM-DD.", output)
        self.assertIn("✅ Insumo aplicado à cultura com sucesso", output)


if __name__ == "__main__":
    unittest.main()
