import os
import sys
import logging

logging_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    Level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("textSummarizerLogger")
"""

root_logger= logging.getLogger(__name__)
root_logger.setLevel(logging.INFO)
handler = logging.FileHandler('running_logs.log', 'a', 'utf-8')
handler.setFormatter(logging.Formatter( ": %(levelname)s:%(asctime)s | %(message)s"))
root_logger.addHandler(handler)
logger=logging.getLogger("textSummarizerLogger")

"""