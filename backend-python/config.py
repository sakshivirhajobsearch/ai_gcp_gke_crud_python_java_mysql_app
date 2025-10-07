import os

# GCP GKE Config
GCP_PROJECT = os.getenv("GCP_PROJECT")
GKE_ZONE = os.getenv("GKE_ZONE")

# MySQL Config
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "admin"
MYSQL_DB = "ai_gcp_gke"
