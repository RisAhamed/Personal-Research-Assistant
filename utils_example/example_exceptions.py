"""
Example demonstrating exception handling with logging.
This shows how exceptions are caught, logged, and displayed with detailed information.
"""

import sys
from logger import logger
from exception import CustomException, handle_exception


def divide_numbers(a, b):
    """Example function that might raise an exception."""
    try:
        logger.info(f"Attempting to divide {a} by {b}")
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except Exception as e:
        raise CustomException(e, sys)


def process_data(data_list, index):
    """Example function accessing list elements."""
    try:
        logger.info(f"Accessing index {index} from list")
        value = data_list[index]
        logger.info(f"Successfully retrieved value: {value}")
        return value
    except Exception as e:
        # Using handle_exception which logs automatically
        exception = handle_exception(e, sys)
        raise exception


def validate_user_input(user_data):
    """Example function with custom validation."""
    try:
        logger.info("Validating user input...")
        
        if user_data is None:
            raise ValueError("User data cannot be None")
        
        if not isinstance(user_data, dict):
            raise TypeError("User data must be a dictionary")
        
        if 'name' not in user_data:
            raise KeyError("User data must contain 'name' field")
        
        logger.info("User input validation passed")
        return True
        
    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    logger.info("Starting exception handling examples...")
    
    # Example 1: Division by zero
    print("\n=== Example 1: Division by Zero ===")
    try:
        divide_numbers(10, 0)
    except CustomException as e:
        print(f"Caught exception: {e}")
    
    # Example 2: Index out of range
    print("\n=== Example 2: Index Out of Range ===")
    try:
        process_data([1, 2, 3], 10)
    except CustomException as e:
        print(f"Caught exception: {e}")
    
    # Example 3: Validation error
    print("\n=== Example 3: Validation Error ===")
    try:
        validate_user_input(None)
    except CustomException as e:
        print(f"Caught exception: {e}")
    
    # Example 4: Successful operations
    print("\n=== Example 4: Successful Operations ===")
    try:
        divide_numbers(10, 2)
        process_data([1, 2, 3], 1)
        validate_user_input({'name': 'John', 'age': 30})
        logger.info("All operations completed successfully!")
    except CustomException as e:
        print(f"Caught exception: {e}")
