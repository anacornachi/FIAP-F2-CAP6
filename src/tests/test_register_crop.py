import unittest
from unittest.mock import patch, mock_open
import sys
import io
import tempfile
import json

from src.crop_manager import register_crop, import_crops_from_json
from src.db.oracle import get_connection


class TestRegisterAndImportCrops(unittest.TestCase):

    def setUp(self):
        self.names_to_clear = ["Milho", "Soja"]
        self._clear_test_data()

    def tearDown(self):
        self._clear_test_data()

    def _clear_test_data(self):
        conn = get_connection()
        cursor = conn.cursor()
        for name in self.names_to_clear:
            cursor.execute("DELETE FROM crops WHERE name = :name", {"name": name})
        conn.commit()
        cursor.close()
        conn.close()

    # Manual
    @patch("builtins.input")
    def test_register_crop_success(self, mock_input):
        mock_input.side_effect = [
            "Milho",
            "2024-09-10",
            "",
            "5.0",
            "7.5",
        ]

        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            register_crop()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("✅ Cultura cadastrada com sucesso!", output)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM crops WHERE name = 'Milho'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        self.assertIsNotNone(result)

    @patch("builtins.input")
    def test_invalid_date_then_correct(self, mock_input):
        mock_input.side_effect = ["Milho", "10-2024-01", "2024-10-10", "", "4.0", "5.5"]
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            register_crop()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌", output)
        self.assertIn("✅ Cultura cadastrada com sucesso!", output)

    @patch("builtins.input")
    def test_negative_area_then_correct(self, mock_input):
        mock_input.side_effect = ["Soja", "2024-08-01", "", "-3.5", "3.5", "6.0"]
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            register_crop()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌", output)
        self.assertIn("✅ Cultura cadastrada com sucesso!", output)

    # Import via json
    @patch("builtins.input")
    def test_valid_import_flow(self, mock_input):
        valid_data = [
            {
                "name": "Soja",
                "planting_date": "2024-08-20",
                "harvest_date": "",
                "area": 3.2,
                "productivity": 6.8,
            }
        ]

        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, suffix=".json"
        ) as tmp_file:
            json.dump(valid_data, tmp_file)
            tmp_file_path = tmp_file.name

        mock_input.return_value = tmp_file_path

        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            import_crops_from_json()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("✅ 1 cultura(s) importada(s) com sucesso.", output)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM crops WHERE name = 'Soja'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        self.assertIsNotNone(result)

    @patch("builtins.input")
    def test_invalid_date_format(self, mock_input):
        data = [
            {
                "name": "Milho",
                "planting_date": "10-10-2024",
                "harvest_date": "",
                "area": 5.0,
                "productivity": 7.2,
            }
        ]

        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, suffix=".json"
        ) as tmp_file:
            json.dump(data, tmp_file)
            tmp_file_path = tmp_file.name

        mock_input.return_value = tmp_file_path

        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            import_crops_from_json()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("❌ Erros no registro 1:", output)
        self.assertIn("planting_date", output)
        self.assertNotIn("✅ 1 cultura(s) importada(s)", output)

    @patch("src.crop_manager.open", new_callable=mock_open, read_data="[]")
    @patch("builtins.input", return_value="fake_path.json")
    def test_import_empty_json(self, mock_input, mock_file):
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output

        try:
            import_crops_from_json()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys_stdout_backup

        self.assertIn("⚠️ Nenhum dado válido encontrado.", output)


if __name__ == "__main__":
    unittest.main()
