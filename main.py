from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DatatTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logging
from textSummarizer.exception import TextException
import sys


# STAGE_NAME = "Data Ingestion stage"
# try:
#    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    data_ingestion = DataIngestionTrainingPipeline()
#    data_ingestion.main()
#    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         raise TextException(e, sys)

# STAGE_NAME = "Data Validation stage"
# try:
#    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    data_validation = DataValidationTrainingPipeline()
#    data_validation.main()
#    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         raise TextException(e, sys)

# STAGE_NAME = "Data Transformation stage"
# try:
#    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    data_transformation = DatatTransformationTrainingPipeline()
#    data_transformation.main()
#    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         raise TextException(e, sys)

# STAGE_NAME = "Model Trainer stage"
# try:
#    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    model_trainer = ModelTrainerTrainingPipeline()
#    model_trainer.main()
#    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         raise TextException(e, sys)

STAGE_NAME = "Model Evaluation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_evluation = ModelEvaluationTrainingPipeline()
   model_evluation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        raise TextException(e, sys)
