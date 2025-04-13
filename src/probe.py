from src.db.oracle import get_connection


def run_probe():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM DUAL")
        result = cursor.fetchone()
        if result and result[0] == 1:
            print("✅ Successfully connected to Oracle Database!")
        else:
            print("⚠️ Oracle responded, but the result was unexpected:", result)
        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Failed to connect to Oracle:", str(e))


if __name__ == "__main__":
    run_probe()
