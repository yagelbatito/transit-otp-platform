import os
import requests
from datetime import datetime
print("START download_gtfs.py")

GTFS_URL = "https://gtfs.mot.gov.il/gtfsfiles/israel-public-transportation.zip"
DATA_DIR = "data"


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def build_output_filename():
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    return f"gtfs_{ts}.zip"


def download_gtfs(output_path):
    response = requests.get(GTFS_URL, timeout=30)

    if response.status_code != 200:
        raise RuntimeError(f"Download failed with status {response.status_code}")

    with open(output_path, "wb") as f:
        f.write(response.content)


def main():
    ensure_data_dir()
    filename = build_output_filename()
    output_path = os.path.join(DATA_DIR, filename)
    download_gtfs(output_path)
    print(f"GTFS downloaded successfully to: {output_path}")


if __name__ == "__main__":
    main()
