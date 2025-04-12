input_schema = {
    "crop_name": {"type": "string", "empty": False},
    "input_type": {"type": "string", "allowed": ["fertilizante", "semente", "defensivo"]},
    "input_name": {"type": "string", "empty": False},
    "quantity": {"type": "float", "min": 0.01},
    "unit": {"type": "string", "allowed": ["kg", "g", "L", "ml", "sacos"]},
    "application_date": {"type": "string", "regex": r"^\d{4}-\d{2}-\d{2}$"}
}
