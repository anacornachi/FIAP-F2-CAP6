from src.db.oracle import get_connection

def get_historical_input_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.area, c.productivity, i.input_name, i.input_type, i.unit, i.unit_price, a.quantity
        FROM crop_input_applications a
        JOIN crops c ON c.id = a.crop_id
        JOIN inputs i ON i.id = a.input_id
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
