import logging
from datetime import datetime
import os

LOG_DIR ="HOUSE_PRICE_LOGS"

Timestamp = f"{datetime.now().strftime('%y-%m-%d_%H-%M-%S')}"
log_file_name =f"Log_{Timestamp}.log"

os.makedirs(LOG_DIR, exist_ok=True)

Log_file_path =os.path.join(LOG_DIR, log_file_name)

logging.basicConfig(
    filename=Log_file_path,
    filemode="w",
    format ="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

#logger = logging.getLogger("House_Price_Logger")