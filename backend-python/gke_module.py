from google.cloud import container_v1
from config import GCP_PROJECT, GKE_ZONE

def list_clusters():
    client = container_v1.ClusterManagerClient()
    parent = f"projects/{GCP_PROJECT}/locations/{GKE_ZONE}"
    clusters = client.list_clusters(parent=parent).clusters
    result = []
    for c in clusters:
        result.append({
            "name": c.name,
            "location": c.location,
            "node_count": c.current_node_count,
            "status": c.status.name
        })
    return result
