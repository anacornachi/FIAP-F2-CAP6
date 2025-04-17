from src.db.oracle import get_connection

def save_input_to_db(data: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO inputs (input_type, input_name, unit, unit_price)
        VALUES (:input_type, :input_name, :unit, :unit_price)
    """, data)

    conn.commit()
    cursor.close()
    conn.close()


def save_input_application_to_db(data: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO crop_input_applications (
            crop_id, input_id, quantity, unit, application_date, recurrence, recurrence_days
        ) VALUES (
            :crop_id, :input_id, :quantity, :unit, TO_DATE(:application_date, 'YYYY-MM-DD'),
            :recurrence, :recurrence_days
        )
    """, data)

    conn.commit()
    cursor.close()
    conn.close()


def get_all_inputs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, input_type, input_name FROM inputs")
    rows = cursor.fetchall()
    columns = [desc[0].lower() for desc in cursor.description]
    cursor.close()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]
