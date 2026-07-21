from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Iniatiation completed")
        print(dataingestionartifact)
        
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validataion=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validataion_artifact=data_validataion.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validataion_artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)