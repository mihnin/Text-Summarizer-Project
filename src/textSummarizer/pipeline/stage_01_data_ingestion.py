# new
from textSummarizer.config.configuration import ConfigurationManager 
# импортируем класс ConfigurationManager из модуля configuration в пакете config в проекте textSummarizer
from textSummarizer.conponents.data_ingestion import DataIngestion 
# импортируем класс DataIngestion из модуля data_ingestion в пакете components в проекте textSummarizer
from textSummarizer.logging import logger 
# импортируем объект logger из модуля logging в проекте textSummarizer

class DataIngestionTrainingPipeline: # создаем класс DataIngestionTrainingPipeline
    def __init__(self): # конструктор класса
        pass # пустой оператор

    def main(self): # создаем метод main()
        config = ConfigurationManager() # создаем экземпляр класса ConfigurationManager 
        #и присваиваем его переменной config
        data_ingestion_config = config.get_data_ingestion_config() # получаем конфигурацию 
        #загрузки данных
        data_ingestion = DataIngestion(config=data_ingestion_config) # создаем экземпляр класса
        data_ingestion.download_file() # вызываем метод download_file() у объекта data_ingestion
        data_ingestion.extract_zip_file() # вызываем метод extract_zip_file() у объекта data_ingestion