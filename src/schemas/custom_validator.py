from cerberus import Validator
import re


class CustomValidator(Validator):

    def _validate_regex_if_not_empty(self, pattern, field, value):
        if value:
            if not re.match(pattern, value):
                self._error(field, "Formato inválido. Use o formato AAAA-MM-DD.")

    def _validate_regex_if_not_empty_arguments(self, rule_argument):
        if not isinstance(rule_argument, str):
            raise ValueError("regex_if_not_empty must be a string.")
