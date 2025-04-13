from src.db.oracle import get_connection


def create_crops_table():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    BEGIN
        EXECUTE IMMEDIATE '
            CREATE TABLE crops (
                id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name VARCHAR2(100) NOT NULL,
                planting_date DATE NOT NULL,
                harvest_date DATE,
                area FLOAT NOT NULL,
                productivity FLOAT NOT NULL
            )
        ';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -955 THEN -- ORA-00955: name is already used by an existing object
                RAISE;
            END IF;
    END;
    """

    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Table 'crops' created (or already exists).")


if __name__ == "__main__":
    create_crops_table()
