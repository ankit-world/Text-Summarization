from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logging
from textSummarizer.exception import TextException
import sys




class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:

            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        
        except Exception as e:
            raise TextException(e, sys)