from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.conponents.data_validation import DataValiadtion
from textSummarizer.logging import logger


class DataValidationTrainingPipeline: # создаем класс DataValidationTrainingPipeline
    def __init__(self): # конструктор класса
        pass

    def main(self): # метод для запуска валидации данных
        config = ConfigurationManager() # создаем объект класса ConfigurationManager
        data_validation_config = config.get_data_validation_config() # получаем конфигурацию валидации данных
        data_validation = DataValiadtion(config=data_validation_config) # создаем объект класса DataValiadtion
        data_validation.validate_all_files_exist() # запускаем валидацию данных