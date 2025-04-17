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
    cursor.execute("SELECT id, name FROM crops")
    rows = cursor.fetchall()
    columns = [desc[0].lower() for desc in cursor.description]
    cursor.close()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]
