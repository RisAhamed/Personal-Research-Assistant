# Logger and Exception Handler Usage Guide

## Overview

This project includes a robust logging system and exception handler that work together to provide comprehensive error tracking and debugging capabilities.

## Features

### Logger System (`logger.py`)
- ✅ **Dual Output**: Displays logs in terminal AND saves to file simultaneously
- ✅ **Timestamped Log Files**: Each run creates a new log file with timestamp
- ✅ **Organized Storage**: All logs saved in `logs/` directory
- ✅ **Multiple Log Levels**: INFO, DEBUG, WARNING, ERROR, CRITICAL
- ✅ **Detailed Format**: Includes timestamp, line number, logger name, and level
- ✅ **Custom Loggers**: Create named loggers for different modules

### Exception Handler (`exception.py`)
- ✅ **Detailed Error Info**: Captures file name, line number, and error message
- ✅ **System Integration**: Uses `sys` module to extract traceback details
- ✅ **Automatic Logging**: Errors are automatically logged when using `handle_exception()`
- ✅ **Custom Exception Class**: `CustomException` with detailed error messages
- ✅ **Easy Import**: Can be used across all files and folders in the project

## Installation

No additional packages required! Both modules use Python standard library.

## Usage

### 1. Basic Logging

```python
from logger import logger

# Different log levels
logger.info("Application started")
logger.debug("Debug information")
logger.warning("Warning message")
logger.error("Error occurred")
logger.critical("Critical issue")
```

### 2. Custom Logger

```python
from logger import get_logger

# Create a custom logger for your module
custom_logger = get_logger("DataProcessing")
custom_logger.info("Processing data...")
```

### 3. Exception Handling - Method 1 (Using CustomException)

```python
import sys
from exception import CustomException

try:
    result = 10 / 0
except Exception as e:
    raise CustomException(e, sys)
```

### 4. Exception Handling - Method 2 (Using handle_exception)

```python
import sys
from exception import handle_exception

try:
    data = [1, 2, 3]
    value = data[10]
except Exception as e:
    # This automatically logs the error and returns the exception
    exception = handle_exception(e, sys)
    raise exception
```

### 5. Complete Example with Both Logger and Exception Handler

```python
import sys
from logger import logger
from exception import CustomException

def process_customer_data(customer_id):
    try:
        logger.info(f"Processing customer: {customer_id}")
        
        # Your processing logic here
        if customer_id is None:
            raise ValueError("Customer ID cannot be None")
        
        logger.info(f"Customer {customer_id} processed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Failed to process customer {customer_id}")
        raise CustomException(e, sys)

# Usage
if __name__ == "__main__":
    try:
        process_customer_data(None)
    except CustomException as e:
        print(f"Error: {e}")
```

## Log File Structure

Logs are saved in the `logs/` directory with the following naming convention:
```
logs/
├── 10_02_2025_18_45_33.log
├── 10_02_2025_19_30_15.log
└── 10_02_2025_20_15_42.log
```

## Log Format

Each log entry follows this format:
```
[ 2025-10-02 18:45:33,163 ] 14 CustomerSupportLogger - INFO - This is an info message
```

Format breakdown:
- **Timestamp**: `2025-10-02 18:45:33,163`
- **Line Number**: `14` (line in source file)
- **Logger Name**: `CustomerSupportLogger`
- **Log Level**: `INFO`
- **Message**: `This is an info message`

## Exception Error Format

Exceptions provide detailed information:
```
Error occurred in script: [C:\path\to\file.py] at line number: [15] - Error message: [division by zero]
```

## Best Practices

1. **Import at the top of your files**:
   ```python
   import sys
   from logger import logger
   from exception import CustomException, handle_exception
   ```

2. **Log important operations**:
   ```python
   logger.info("Starting data processing")
   # ... your code ...
   logger.info("Data processing completed")
   ```

3. **Always use try-except for critical operations**:
   ```python
   try:
       # risky operation
   except Exception as e:
       raise CustomException(e, sys)
   ```

4. **Use appropriate log levels**:
   - `DEBUG`: Detailed debugging information
   - `INFO`: General informational messages
   - `WARNING`: Warning messages for potentially harmful situations
   - `ERROR`: Error messages for serious problems
   - `CRITICAL`: Critical messages for very serious errors

## Examples

Run the example files to see the system in action:

```bash
# Basic logging examples
python example_usage.py

# Exception handling examples
python example_exceptions.py
```

## Benefits

1. **Easy Debugging**: Know exactly where errors occur (file and line number)
2. **Complete Audit Trail**: All logs saved with timestamps
3. **Real-time Monitoring**: See logs in terminal while they're being saved
4. **Consistent Error Handling**: Standardized error messages across the project
5. **Production Ready**: Suitable for development and production environments

## Notes

- The `logs/` directory is created automatically on first run
- Each script execution creates a new log file
- Both terminal output and file logging happen simultaneously
- The exception handler integrates seamlessly with the logger
- All modules are importable from any file or folder in the project
