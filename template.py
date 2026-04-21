import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "index.html",
    "css/style.css",
    "js/main.js",
    "images/.gitkeep",
    "README.md",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"Skipped (already has content): {filename}")

logging.info("✅ Portfolio structure created successfully!")