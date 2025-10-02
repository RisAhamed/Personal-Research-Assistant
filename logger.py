import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # Save to file
        logging.StreamHandler()  # Display in terminal
    ]
)

# Create a logger instance
logger = logging.getLogger("CustomerSupportLogger")


def get_logger(name: str = "CustomerSupportLogger"):
    """
    Get a logger instance with the specified name.
    
    Args:
        name (str): Name of the logger. Defaults to "CustomerSupportLogger".
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    return logging.getLogger(name)


# Export the logger for easy import
__all__ = ['logger', 'get_logger']
