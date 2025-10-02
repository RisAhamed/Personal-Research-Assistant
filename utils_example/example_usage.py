"""
Example usage of the logger and exception handler modules.
This demonstrates how to import and use the logger and exception handler
from other files in your project.
"""

import sys
from logger import logger, get_logger
from exception import CustomException, handle_exception


def example_logging():
    """Demonstrate various logging levels."""
    logger.info("This is an info message - application started")
    logger.debug("This is a debug message - for detailed debugging")
    logger.warning("This is a warning message - something to watch out for")
    logger.error("This is an error message - something went wrong")
    logger.critical("This is a critical message - serious problem")


def example_basic_exception():
    """Demonstrate basic exception handling."""
    try:
        # Simulate an error
        result = 10 / 0
    except Exception as e:
        # Method 1: Using CustomException directly
        raise CustomException(e, sys)


def example_exception_with_handler():
    """Demonstrate exception handling with the handle_exception function."""
    try:
        # Simulate another error
        data = [1, 2, 3]
        value = data[10]  # Index out of range
    except Exception as e:
        # Method 2: Using handle_exception function (logs and returns exception)
        exception = handle_exception(e, sys)
        raise exception


def example_custom_error_message():
    """Demonstrate custom error messages."""
    try:
        # Simulate validation error
        user_input = None
        if user_input is None:
            raise ValueError("User input cannot be None")
    except Exception as e:
        raise CustomException(e, sys)


def example_with_custom_logger():
    """Demonstrate using a custom logger name."""
    custom_logger = get_logger("DataProcessing")
    custom_logger.info("Processing customer data...")
    custom_logger.info("Data validation completed")


if __name__ == "__main__":
    # Example 1: Basic logging
    print("\n=== Example 1: Basic Logging ===")
    example_logging()
    
    # Example 2: Custom logger
    print("\n=== Example 2: Custom Logger ===")
    example_with_custom_logger()
    
    # Example 3: Exception handling (uncomment to test)
    # print("\n=== Example 3: Basic Exception ===")
    # example_basic_exception()
    
    # Example 4: Exception with handler (uncomment to test)
    # print("\n=== Example 4: Exception with Handler ===")
    # example_exception_with_handler()
    
    # Example 5: Custom error message (uncomment to test)
    # print("\n=== Example 5: Custom Error Message ===")
    # example_custom_error_message()
    
    logger.info("Example execution completed successfully!")
