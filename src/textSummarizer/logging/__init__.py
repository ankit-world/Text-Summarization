import os
import sys
import logging
from from_root import from_root
from datetime import datetime

# logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# log_dir = "logs"
# log_filepath = os.path.join(log_dir,"running_logs.log")
# os.makedirs(log_dir, exist_ok=True)



# logging.basicConfig(
#     level= logging.INFO,
#     format= logging_str,

#     handlers=[
#         logging.FileHandler(log_filepath),
#         logging.StreamHandler(sys.stdout)
#     ]
# )

# logger = logging.getLogger("textSummarizerLogger")

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)