from src.db.oracle import get_connection


def save_crop_to_db(crop_data):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO crops (name, planting_date, harvest_date, area, productivity)
        VALUES (:name, TO_DATE(:planting_date, 'YYYY-MM-DD'), TO_DATE(:harvest_date, 'YYYY-MM-DD'), :area, :productivity)
        """

        harvest_date = crop_data.get("harvest_date") or None

        cursor.execute(
            sql,
            {
                "name": crop_data["name"],
                "planting_date": crop_data["planting_date"],
                "harvest_date": harvest_date,
                "area": crop_data["area"],
                "productivity": crop_data["productivity"],
            },
        )

        conn.commit()
        print("🗂️ Salvo com sucesso no banco de dados.")

    except Exception as e:
        print("❌ Falha ao salvar a cultura no banco de dados.")
        print(f"📎 Erro: {str(e)}")

    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals():
            conn.close()


def get_all_crops():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, planting_date, harvest_date, area, productivity
        FROM crops
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "planting_date": row[2],
            "harvest_date": row[3],
            "area": row[4],
            "productivity": row[5]
        }
        for row in rows
    ]


def update_crop_harvest_date(crop_id: int, harvest_date: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
                UPDATE crops
                SET harvest_date = TO_DATE(:harvest_date, 'YYYY-MM-DD')
                WHERE id = :crop_id
            """, {"harvest_date": harvest_date, "crop_id": crop_id})
        conn.commit()
    finally:
        cursor.close()
        conn.close()