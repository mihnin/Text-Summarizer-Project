from textSummarizer.config.configuration import ConfigurationManager 
# импортировать класс для работы с конфигурацией
from textSummarizer.conponents.model_trainer import ModelTrainer # импортировать класс для обучения модели
from textSummarizer.logging import logger # импортировать класс для логирования


class ModelTrainerTrainingPipeline: # класс для обучения модели
    def __init__(self): # конструктор класса
        pass # пустой оператор

    def main(self): # метод для обучения модели
        config = ConfigurationManager() # создать объект для работы с конфигурацией
        model_trainer_config = config.get_model_trainer_config() # получить конфигурацию для обучения модели
        model_trainer_config = ModelTrainer(config=model_trainer_config) # создать объект для обучения модели
        model_trainer_config.train() # обучить модель