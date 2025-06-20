from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME='Data Ingestion stage'
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ing=DataIngestionTrainingPipeline()
    data_ing.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation stage'
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_val = DataValidationTrainingPipeline()
    data_val.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Data Transformation stage'
try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<<<")
    data_trans=DataTransformationTrainingPipeline()
    data_trans.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Traniner stage'
try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<<<")
    model_trainer=ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Model Evaluation stage'
try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<<<")
    data_eval=ModelEvaluationTrainingPipeline()
    data_eval.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e