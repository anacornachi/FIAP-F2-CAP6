crop_schema = {
    "name": {"type": "string", "empty": False},
    "planting_date": {"type": "string", "regex": r"^\d{4}-\d{2}-\d{2}$"},
    "harvest_date": {"type": "string", "regex": r"^\d{4}-\d{2}-\d{2}$", "nullable": True},
    "area": {"type": "float", "min": 0},
    "productivity": {"type": "float", "min": 0}
}
