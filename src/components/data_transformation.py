import os
import sys
import pandas as pd
import dill 

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from dataclasses import dataclass

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from exception import CustomException
from logger import logging



@dataclass
class DataTransformationConfig:
    """Configuration class for data transformation."""
    # Define the path where we'll save our preprocessing object
    preprocessor_obj_file_path: str = os.path.join('saved_models', 'preprocessor.pkl')

class DataTransformation:
    """
    This class handles the data transformation process, including train-test split
    and building the preprocessing pipeline.
    """
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        Creates and returns a Scikit-learn ColumnTransformer object.
        This object defines the preprocessing steps for our text data.
        """
        try:
            logging.info("Creating data transformer object")
            
            text_feature = "text"
            
            # Create a pipeline just for the text feature
            text_pipeline = Pipeline(steps=[
                ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000))
            ])
            
      
            preprocessor = ColumnTransformer(
                transformers=[
                    ('text_trans', text_pipeline, [text_feature])
                ],
                remainder='passthrough' # Keep other columns if any (we don't have them now)
            )
            
            logging.info("Data transformer object created successfully")
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, data_path):
        """
        Loads data, performs train-test split, applies the preprocessing pipeline,
        and saves the preprocessing object.
        """
        try:
            logging.info("Data transformation initiated")
            
            df = pd.read_csv(data_path)
            
            # For this model, we need the 'text' as our feature (X) and 'category' as our target (y)
            X = df[['text']]
            y = df['category']
            
            logging.info("Performing train-test split")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
            
            preprocessor_obj = self.get_data_transformer_object()
            
            logging.info("Fitting preprocessing object on training data")
            # Fit the preprocessor on the training data and transform it
            X_train_processed = preprocessor_obj.fit_transform(X_train)
            
            logging.info("Transforming test data")
            # Transform the test data using the already-fitted preprocessor
            X_test_processed = preprocessor_obj.transform(X_test)
            
            logging.info(f"Saving preprocessing object to: {self.data_transformation_config.preprocessor_obj_file_path}")
            # Save the fitted preprocessor object for later use in our prediction pipeline
            with open(self.data_transformation_config.preprocessor_obj_file_path, "wb") as file_obj:
                dill.dump(preprocessor_obj, file_obj)

            logging.info("Data transformation completed successfully")
            
            return (
                X_train_processed,
                X_test_processed,
                y_train,
                y_test,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)
