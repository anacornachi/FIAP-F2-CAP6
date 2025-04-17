input_schema = {
    "input_type": {
        "type": "string",
        "required": True,
        "allowed": ["fertilizante", "semente", "defensivo", "adubo"]
    },
    "input_name": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "unit": {
        "type": "string",
        "required": True,
        "allowed": ["kg", "g", "l", "ml", "sacos"]
    },
    "unit_price": {
        "type": "float",
        "required": True,
        "min": 0.01,
        "coerce": float
    }
}
