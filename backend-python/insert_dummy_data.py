from mysql_module import get_connection

def insert_dummy_clusters():
    dummy_clusters = [
        {"name": "cluster-alpha", "location": "us-central1", "node_count": 3, "status": "RUNNING"},
        {"name": "cluster-beta", "location": "europe-west1", "node_count": 12, "status": "RUNNING"},
        {"name": "cluster-gamma", "location": "asia-east1", "node_count": 1, "status": "STOPPED"},
        {"name": "cluster-delta", "location": "us-east1", "node_count": 5, "status": "RUNNING"},
        {"name": "cluster-epsilon", "location": "southamerica-east1", "node_count": 15, "status": "RUNNING"}
    ]

    try:
        conn = get_connection()
        cursor = conn.cursor()

        for c in dummy_clusters:
            cursor.execute("""
            INSERT INTO clusters (name, location, node_count, status)
            VALUES (%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE node_count=%s, status=%s
            """, (c["name"], c["location"], c["node_count"], c["status"],
                  c["node_count"], c["status"]))

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Dummy cluster data inserted successfully!")

    except Exception as e:
        print(f"❌ Error inserting dummy data: {e}")

if __name__ == "__main__":
    insert_dummy_clusters()
