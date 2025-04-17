application_schema = {
    "crop_id": {"type": "integer", "required": True, "min": 1},
    "input_id": {"type": "integer", "required": True, "min": 1},
    "quantity": {"type": "float", "required": True, "min": 0.01, "coerce": float},
    "unit": {
        "type": "string",
        "required": True,
        "allowed": ["kg", "g", "L", "ml", "sacos"]
    },
    "application_date": {
        "type": "string",
        "required": True,
        "regex_if_not_empty": r"^\d{4}-\d{2}-\d{2}$"
    },
    "recurrence": {
        "type": "string",
        "required": False,
        "allowed": ["única", "semanal", "quinzenal", "mensal"]
    },
    "recurrence_days": {
        "type": "integer",
        "required": False,
        "min": 1
    }
}
