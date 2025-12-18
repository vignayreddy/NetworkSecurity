from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig




if __name__=='__main__':
    try:
        trainingpipelienconfig = TrainingPipelineConfig()
        
        dataingestionconfig = DataIngestionConfig(trainingpipelienconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Inititate the data Ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
           raise NetworkSecurityException(e,sys)