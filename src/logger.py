import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
def get_log_file_path():
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_file = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
    return os.path.join(logs_dir, log_file)

LOG_FILE = get_log_file_path()

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logger is working!")
    