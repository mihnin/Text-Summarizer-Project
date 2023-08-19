from textSummarizer.config.configuration import ConfigurationManager # импортируем класс конфигурации
from textSummarizer.conponents.data_transformation import DataTransformation 
# импортируем класс преобразования данных
from textSummarizer.logging import logger # импортируем логгер


class DataTransformationTrainingPipeline: # создаем класс DataTransformationTrainingPipeline
    def __init__(self): # конструктор класса
        pass # пустой блок

    def main(self): # метод для преобразования данных
        config = ConfigurationManager() # создаем объект класса ConfigurationManager
        data_transformation_config = config.get_data_transformation_config() 
        # получаем конфигурацию преобразования данных
        data_transformation = DataTransformation(config=data_transformation_config) 
        # создаем объект класса DataTransformation
        data_transformation.convert() # преобразуем данные