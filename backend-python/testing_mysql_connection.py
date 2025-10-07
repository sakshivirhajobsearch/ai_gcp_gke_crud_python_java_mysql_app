from mysql_module import get_connection

def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()[0]
        print(f"✅ Connected to MySQL database: {db_name}")

        # Check if clusters table exists
        cursor.execute("SHOW TABLES LIKE 'clusters';")
        result = cursor.fetchone()
        if result:
            print("✅ 'clusters' table exists.")
        else:
            print("⚠️ 'clusters' table does NOT exist. Please run init_db() in mysql_module.py")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error connecting to MySQL: {e}")

if __name__ == "__main__":
    test_connection()
