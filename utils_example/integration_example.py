"""
Integration Example: Customer Support Agent
This demonstrates how to integrate the logger and exception handler 
into your actual customer support application.
"""

import sys
import pandas as pd
from logger import logger
from exception import CustomException, handle_exception


class CustomerSupportAgent:
    """Example class showing integration of logger and exception handler."""
    
    def __init__(self, data_path=None):
        """Initialize the customer support agent."""
        logger.info("Initializing Customer Support Agent")
        self.data_path = data_path
        self.data = None
        
    def load_data(self):
        """Load customer support data from CSV."""
        try:
            logger.info(f"Loading data from: {self.data_path}")
            
            if self.data_path is None:
                raise ValueError("Data path cannot be None")
            
            self.data = pd.read_csv(self.data_path)
            logger.info(f"Successfully loaded {len(self.data)} records")
            logger.info(f"Columns: {list(self.data.columns)}")
            
            return self.data
            
        except FileNotFoundError as e:
            logger.error(f"File not found: {self.data_path}")
            raise CustomException(e, sys)
        except pd.errors.EmptyDataError as e:
            logger.error("The CSV file is empty")
            raise CustomException(e, sys)
        except Exception as e:
            logger.error("Failed to load data")
            raise CustomException(e, sys)
    
    def analyze_data(self):
        """Analyze the customer support data."""
        try:
            logger.info("Starting data analysis")
            
            if self.data is None:
                raise ValueError("No data loaded. Call load_data() first.")
            
            # Example analysis
            logger.info(f"Data shape: {self.data.shape}")
            logger.info(f"Data info:\n{self.data.info()}")
            
            # Check for missing values
            missing = self.data.isnull().sum()
            if missing.any():
                logger.warning(f"Missing values found:\n{missing[missing > 0]}")
            else:
                logger.info("No missing values found")
            
            logger.info("Data analysis completed successfully")
            
        except Exception as e:
            logger.error("Data analysis failed")
            raise CustomException(e, sys)
    
    def process_query(self, query):
        """Process a customer support query."""
        try:
            logger.info(f"Processing query: {query[:50]}...")
            
            if not query or query.strip() == "":
                raise ValueError("Query cannot be empty")
            
            # Simulate processing
            logger.info("Query processed successfully")
            
            return {"status": "success", "query": query}
            
        except Exception as e:
            logger.error("Query processing failed")
            exception = handle_exception(e, sys)
            raise exception


def main():
    """Main function demonstrating the integration."""
    logger.info("="*60)
    logger.info("Customer Support Agent - Starting")
    logger.info("="*60)
    
    # Example 1: Successful workflow
    print("\n=== Example 1: Successful Data Loading ===")
    try:
        agent = CustomerSupportAgent(data_path="twcs/sample.csv")
        data = agent.load_data()
        logger.info("First few rows:")
        print(data.head())
    except CustomException as e:
        logger.error(f"Failed: {e}")
        print(f"Error: {e}")
    
    # Example 2: Error handling - missing file
    print("\n=== Example 2: File Not Found Error ===")
    try:
        agent = CustomerSupportAgent(data_path="nonexistent_file.csv")
        agent.load_data()
    except CustomException as e:
        print(f"Caught error: {e}")
    
    # Example 3: Query processing
    print("\n=== Example 3: Query Processing ===")
    try:
        agent = CustomerSupportAgent()
        result = agent.process_query("How do I reset my password?")
        logger.info(f"Result: {result}")
    except CustomException as e:
        print(f"Error: {e}")
    
    # Example 4: Empty query error
    print("\n=== Example 4: Empty Query Error ===")
    try:
        agent = CustomerSupportAgent()
        agent.process_query("")
    except CustomException as e:
        print(f"Caught error: {e}")
    
    logger.info("="*60)
    logger.info("Customer Support Agent - Completed")
    logger.info("="*60)


if __name__ == "__main__":
    main()
