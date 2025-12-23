from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation



if __name__=='__main__':
    try:
        trainingpipelienconfig = TrainingPipelineConfig()
        

        #Ingestion

        dataingestionconfig = DataIngestionConfig(trainingpipelienconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Inititate the data Ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Compeleted")
        print(dataingestionartifact)



        #Validation

        data_validation_config = DataValidationConfig(trainingpipelienconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed ")


        #Transformation
        data_transformation_config = DataTransformationConfig(trainingpipelienconfig)
        logging.info("Data Transformation Initialized ")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed ")
        print(data_transformation_artifact)
        

    except Exception as e:
           raise NetworkSecurityException(e,sys)