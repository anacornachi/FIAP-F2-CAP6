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
    cursor.execute("""
        SELECT id, input_name, input_type, unit, unit_price
        FROM inputs
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "id": row[0],
            "input_name": row[1],
            "input_type": row[2],
            "unit": row[3],
            "unit_price": row[4]
        }
        for row in rows
    ]

def get_input_by_id(input_id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT unit FROM inputs WHERE id = :id", {"id": input_id})
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return {"unit": row[0]} if row else None

def get_applications_by_crop_id(crop_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT i.input_name, i.input_type, a.quantity, a.unit, a.application_date
        FROM crop_input_applications a
        JOIN inputs i ON i.id = a.input_id
        WHERE a.crop_id = :crop_id
    """, {"crop_id": crop_id})

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "input_name": row[0],
            "input_type": row[1],
            "quantity": row[2],
            "unit": row[3],
            "application_date": row[4],
        }
        for row in rows
    ]

def get_applications_by_input_id(input_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.name, a.quantity, a.unit, a.application_date
        FROM crop_input_applications a
        JOIN crops c ON c.id = a.crop_id
        WHERE a.input_id = :input_id
    """, {"input_id": input_id})

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "crop_name": row[0],
            "quantity": row[1],
            "unit": row[2],
            "application_date": row[3],
        }
        for row in rows
    ]