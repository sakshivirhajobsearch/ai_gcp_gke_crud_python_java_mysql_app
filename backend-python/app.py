from flask import Flask, jsonify
from mysql_module import init_db, get_connection
from gke_module import list_clusters as fetch_clusters_gke
from ai_module import analyze_clusters

# Create Flask app
app = Flask(__name__)

# Initialize DB (creates 'clusters' table if not exists)
init_db()

# Home route
@app.route("/")
def home():
    return "✅ GKE CRUD API is running. Use /gke/clusters to fetch cluster data."

# Handle favicon requests
@app.route("/favicon.ico")
def favicon():
    return "", 204

# GKE clusters route
@app.route("/gke/clusters", methods=["GET"])
def get_clusters():
    try:
        # 1️⃣ Fetch clusters from GKE
        try:
            clusters = fetch_clusters_gke()
            if not clusters:
                raise Exception("No clusters found from GKE")
        except Exception as e:
            print("⚠️ GKE API failed, using dummy clusters:", e)
            # Dummy clusters for development/testing
            clusters = [
                {"name": "cluster-alpha", "location": "us-central1", "node_count": 3, "status": "RUNNING"},
                {"name": "cluster-beta", "location": "europe-west1", "node_count": 12, "status": "RUNNING"},
                {"name": "cluster-gamma", "location": "asia-east1", "node_count": 1, "status": "STOPPED"},
                {"name": "cluster-delta", "location": "us-east1", "node_count": 5, "status": "RUNNING"},
                {"name": "cluster-epsilon", "location": "southamerica-east1", "node_count": 15, "status": "RUNNING"}
            ]

        # 2️⃣ Save/update clusters in MySQL
        conn = get_connection()
        cursor = conn.cursor()
        for c in clusters:
            cursor.execute("""
            INSERT INTO clusters (name, location, node_count, status)
            VALUES (%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE node_count=%s, status=%s
            """, (c["name"], c["location"], c["node_count"], c["status"],
                  c["node_count"], c["status"]))
        conn.commit()
        cursor.close()
        conn.close()

        # 3️⃣ AI analysis
        anomalies, suggestions = analyze_clusters(clusters)

        # 4️⃣ Return response
        return jsonify({
            "clusters": clusters,
            "anomalies": anomalies,
            "suggestions": suggestions
        })

    except Exception as e:
        print("Error in /gke/clusters:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
