from src.db.oracle import get_connection

def drop_all_tables():
    conn = get_connection()
    cursor = conn.cursor()

    tables = ["crop_input_applications", "inputs", "crops"]

    for table in tables:
        plsql = f"""
        BEGIN
            EXECUTE IMMEDIATE 'DROP TABLE {table} CASCADE CONSTRAINTS';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -942 THEN -- ORA-00942: table or view does not exist
                    RAISE;
                END IF;
        END;
        """
        cursor.execute(plsql)
        print(f"🗑️ Tabela '{table}' dropada (ou já não existia).")

    conn.commit()
    cursor.close()
    conn.close()



def execute_create_table(sql: str, table_name: str):
    conn = get_connection()
    cursor = conn.cursor()

    plsql = f"""
    BEGIN
        EXECUTE IMMEDIATE q'[{sql}]';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -955 THEN -- ORA-00955: name is already used
                RAISE;
            END IF;
    END;
    """

    cursor.execute(plsql)
    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Table '{table_name}'created (or already exists).")


def create_crops_table():
    sql = """
        CREATE TABLE crops (
            id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            name VARCHAR2(100) NOT NULL,
            planting_date DATE NOT NULL,
            harvest_date DATE,
            area FLOAT NOT NULL,
            productivity FLOAT NOT NULL
        )
    """
    execute_create_table(sql, "crops")


def create_inputs_table():
    sql = """
        CREATE TABLE inputs (
            id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            input_type VARCHAR2(20) NOT NULL,
            input_name VARCHAR2(100) NOT NULL,
            unit VARCHAR2(10) NOT NULL,
            unit_price FLOAT NOT NULL
        )
    """
    execute_create_table(sql, "inputs")


def create_crop_input_applications_table():
    sql = """
        CREATE TABLE crop_input_applications (
            id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            crop_id NUMBER,
            input_id NUMBER,
            quantity FLOAT NOT NULL,
            unit VARCHAR2(10) NOT NULL,
            application_date DATE NOT NULL,
            recurrence VARCHAR2(20),
            recurrence_days NUMBER,
            CONSTRAINT fk_crop FOREIGN KEY (crop_id) REFERENCES crops(id),
            CONSTRAINT fk_input FOREIGN KEY (input_id) REFERENCES inputs(id)
        )
    """
    execute_create_table(sql, "crop_input_applications")


def create_all_tables():
    create_crops_table()
    create_inputs_table()
    create_crop_input_applications_table()


if __name__ == "__main__":
    drop_all_tables()
    create_all_tables()
