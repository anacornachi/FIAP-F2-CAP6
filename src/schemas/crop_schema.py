crop_schema = {
    "name": {"type": "string", "required": True, "empty": False},
    "planting_date": {
        "type": "string",
        "required": True,
        "empty": False,
        "regex": r"^\d{4}-\d{2}-\d{2}$",
    },
    "harvest_date": {
        "type": "string",
        "required": False,
        "nullable": True,
        "empty": True,
        "regex_if_not_empty": r"^\d{4}-\d{2}-\d{2}$",
    },
    "area": {"type": "float", "required": True, "min": 0.01, "coerce": float},
    "productivity": {"type": "float", "required": True, "min": 0.01, "coerce": float},
}
