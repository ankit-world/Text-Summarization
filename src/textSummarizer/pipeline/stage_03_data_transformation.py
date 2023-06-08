from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logging
from textSummarizer.exception import TextException
import sys

class DatatTransformationTrainingPipeline:
    def __init__(self):
        pass

    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e
