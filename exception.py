import sys
from logger import logger


class CustomException(Exception):
    """
    Custom exception class that captures detailed error information
    including the error message, file name, and line number.
    """
    
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the custom exception.
        
        Args:
            error_message: The error message (can be string or Exception object)
            error_detail: sys module to extract exception details
        """
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)
    
    @staticmethod
    def get_detailed_error_message(error_message, error_detail: sys) -> str:
        """
        Extract detailed error information including file name and line number.
        
        Args:
            error_message: The original error message
            error_detail: sys module containing exception information
        
        Returns:
            str: Formatted error message with file and line details
        """
        _, _, exc_tb = error_detail.exc_info()
        
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            
            error_msg = f"Error occurred in script: [{file_name}] at line number: [{line_number}] - Error message: [{str(error_message)}]"
        else:
            error_msg = f"Error message: [{str(error_message)}]"
        
        return error_msg
    
    def __str__(self):
        """Return the detailed error message when the exception is printed."""
        return self.error_message


def handle_exception(error_message, error_detail: sys = sys):
    """
    Handle and log exceptions with detailed information.
    
    Args:
        error_message: The error message or exception object
        error_detail: sys module to extract exception details (defaults to sys)
    
    Returns:
        CustomException: Custom exception object with detailed error information
    """
    exception = CustomException(error_message, error_detail)
    logger.error(exception.error_message)
    return exception


# Export for easy import
__all__ = ['CustomException', 'handle_exception']
