import unittest
from unittest.mock import patch
from src.validations import prompt_and_validate
from src.schemas.crop_schema import crop_schema


class TestPromptAndValidate(unittest.TestCase):

    @patch("builtins.input")
    def test_retry_on_invalid_float_field(self, mock_input):

        mock_input.side_effect = [
            "Milho",
            "2024-10-15",
            "2025-02-10",
            "cinco",
            "5.0",
            "8.5",
        ]

        with patch("builtins.print") as mock_print:
            result = prompt_and_validate(
                crop_schema,
                ["name", "planting_date", "harvest_date", "area", "productivity"],
            )

        self.assertEqual(
            result,
            {
                "name": "Milho",
                "planting_date": "2024-10-15",
                "harvest_date": "2025-02-10",
                "area": 5.0,
                "productivity": 8.5,
            },
        )

        printed_msgs = [call.args[0] for call in mock_print.call_args_list]
        float_error_msgs = [
            msg
            for msg in printed_msgs
            if "❌ Valor inválido. Digite um número com ponto decimal." in msg
        ]
        self.assertTrue(float_error_msgs)

    @patch("builtins.input")
    def test_allow_blank_nullable_field(self, mock_input):

        mock_input.side_effect = ["Feijão", "2024-09-01", "", "2.0", "3.5"]

        result = prompt_and_validate(
            crop_schema,
            ["name", "planting_date", "harvest_date", "area", "productivity"],
        )

        self.assertEqual(
            result,
            {
                "name": "Feijão",
                "planting_date": "2024-09-01",
                "harvest_date": None,
                "area": 2.0,
                "productivity": 3.5,
            },
        )

    @patch("builtins.input")
    def test_invalid_date_format_then_valid(self, mock_input):
        mock_input.side_effect = [
            "Milho",
            "15-10-2024",
            "2024-10-15",
            "",
            "4.5",
            "7.2",
        ]

        with patch("builtins.print") as mock_print:
            result = prompt_and_validate(
                crop_schema,
                ["name", "planting_date", "harvest_date", "area", "productivity"],
            )

        self.assertEqual(
            result,
            {
                "name": "Milho",
                "planting_date": "2024-10-15",
                "harvest_date": None,
                "area": 4.5,
                "productivity": 7.2,
            },
        )

        printed_msgs = [
            " ".join(str(arg) for arg in call.args)
            for call in mock_print.call_args_list
        ]

        date_error_msgs = [
            msg
            for msg in printed_msgs
            if "❌ Formato inválido. Use o formato AAAA-MM-DD." in msg
        ]

        self.assertTrue(
            date_error_msgs, "Esperado erro de formato de data não ocorreu."
        )


if __name__ == "__main__":
    unittest.main()
