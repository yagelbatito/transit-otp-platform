import os
import zipfile
from datetime import datetime

DATA_DIR = "data"
BRONZE_DIR = os.path.join(DATA_DIR, "bronze", "gtfs_static")


def get_latest_gtfs_zip():
    """
    Find the latest downloaded GTFS ZIP file in DATA_DIR.
    """
    files = [
        f for f in os.listdir(DATA_DIR)
        if f.startswith("gtfs_") and f.endswith(".zip")
    ]

    if not files:
        raise FileNotFoundError("No GTFS ZIP files found in data directory.")

    # Choose the newest file by creation time
    latest_file = max(
        files,
        key=lambda f: os.path.getctime(os.path.join(DATA_DIR, f))
    )

    return os.path.join(DATA_DIR, latest_file)


def build_bronze_output_dir():
    """
    Build Bronze output directory partitioned by ingest_date.
    Example:
    data/bronze/gtfs_static/ingest_date=YYYY-MM-DD
    """
    ingest_date = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(BRONZE_DIR, f"ingest_date={ingest_date}")


def extract_zip(zip_path, output_dir):
    """
    Extract GTFS ZIP contents into output_dir.
    """
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)


def main():
    zip_path = get_latest_gtfs_zip()
    output_dir = build_bronze_output_dir()

    os.makedirs(output_dir, exist_ok=True)
    extract_zip(zip_path, output_dir)

    print(f"GTFS extracted to Bronze at: {output_dir}")


if __name__ == "__main__":
    main()
