import unittest
from unittest.mock import patch
import io
import sys
import os

from src.input_manager import register_input, import_inputs_from_json, apply_input_to_crop
from src.db.oracle import get_connection
from src.repositories.crop import get_all_crops
from src.repositories.input import get_all_inputs

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(CURRENT_DIR, "../data/insumos.json")
CROPS_FILE = os.path.join(CURRENT_DIR, "../data/culturas.json")


class TestInputManagement(unittest.TestCase):

    def setUp(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM crop_input_applications")
        cursor.execute("DELETE FROM inputs WHERE input_name IN ('NPK 4-14-8', 'Milho Híbrido', 'Produto X')")
        cursor.execute("DELETE FROM crops WHERE name = 'Milho'")
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
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            register_input()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("✅ Insumo cadastrado com sucesso", output)

    @patch("builtins.input", return_value=INPUT_FILE)
    def test_import_inputs_success(self, mock_input):
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            import_inputs_from_json()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("✅ 2 insumo(s) importado(s) com sucesso", output)

    @patch("builtins.input", return_value=INPUT_FILE)
    def test_import_inputs_with_error(self, mock_input):
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            import_inputs_from_json()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertTrue("❌" in output or "Erros no registro" in output)

    @patch("builtins.input")
    def test_apply_input_to_crop_success(self, mock_input):
        inputs = get_all_inputs()
        crops = get_all_crops()
        if not inputs or not crops:
            self.skipTest("Insumos e culturas devem estar cadastrados antes deste teste.")

        mock_input.side_effect = [
            str(crops[0]["id"]),
            str(inputs[0]["id"]),
            "10",
            "2024-11-01",
            "semanal",
            "7"
        ]

        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            apply_input_to_crop()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("✅ Insumo aplicado à cultura com sucesso", output)


    @patch("builtins.input")
    def test_register_input_missing_name(self, mock_input):
        mock_input.side_effect = ["fertilizante", "", "kg", "4.5", "n"]
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            register_input()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Este campo não pode ficar em branco.", output)

    @patch("builtins.input")
    def test_register_input_invalid_unit(self, mock_input):
        mock_input.side_effect = ["fertilizante", "Produto X", "kilo", "4.5", "n"]
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            register_input()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Valor não permitido. Escolha uma das opções válidas.", output)

    @patch("builtins.input")
    def test_register_input_invalid_price_format(self, mock_input):
        mock_input.side_effect = ["fertilizante", "Produto X", "kg", "abc", "4.5", "n"]
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            register_input()
            output = captured_output.getvalue()
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

        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            apply_input_to_crop()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Formato inválido. Use o formato AAAA-MM-DD.", output)

    def test_apply_input_to_nonexistent_crop(self):
        conn = get_connection()
        cursor = conn.cursor()

        with self.assertRaises(Exception):
            cursor.execute("""
                INSERT INTO crop_input_applications (crop_id, input_id, quantity, unit, application_date)
                VALUES (9999, 9999, 10, 'kg', TO_DATE('2024-10-10', 'YYYY-MM-DD'))
            """)
            conn.commit()

        cursor.close()
        conn.close()
