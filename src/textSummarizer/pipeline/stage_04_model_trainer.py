from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logging
from textSummarizer.exception import TextException
import sys


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise TextException(e, sys)