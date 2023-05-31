import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s:')

project_name = "textSummarizer"

list_of_files =  [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    #f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py"
    f"{project_name}/constants/__init__.py",
    #f"{project_name}/data_access/__init__.py",
    f"{project_name}/entity/__init__.py",
    #f"{project_name}/ml/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/common.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logging/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass # creating an empty file only
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} is already exists")