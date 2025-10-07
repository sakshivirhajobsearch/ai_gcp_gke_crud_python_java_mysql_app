# ai_module.py
from sklearn.ensemble import IsolationForest

def analyze_clusters(clusters):
    """
    Analyze clusters for anomalies and scaling suggestions.
    clusters: list of dicts [{name, location, node_count, status}]
    returns: anomalies list and suggestions list
    """
    anomalies = []
    suggestions = []

    if not clusters:
        return anomalies, suggestions

    # Prepare data for anomaly detection
    node_counts = [[c["node_count"]] for c in clusters]

    # Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(node_counts)
    predictions = model.predict(node_counts)

    for idx, cluster in enumerate(clusters):
        if predictions[idx] == -1:
            anomalies.append(f"Anomaly detected in cluster: {cluster['name']} with node count {cluster['node_count']}")

        # Simple scaling suggestion
        if cluster["node_count"] < 2:
            suggestions.append(f"Consider scaling up cluster: {cluster['name']}")
        elif cluster["node_count"] > 10:
            suggestions.append(f"Consider scaling down cluster: {cluster['name']}")

    return anomalies, suggestions
