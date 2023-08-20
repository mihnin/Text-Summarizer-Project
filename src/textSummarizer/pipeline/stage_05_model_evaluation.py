from textSummarizer.config.configuration import ConfigurationManager # импортируем конфигурацию
from textSummarizer.conponents.model_evaluation import ModelEvaluation # импортируем класс для оценки модели
from textSummarizer.logging import logger # импортируем логгер




class ModelEvaluationTrainingPipeline: # класс для оценки модели
    def __init__(self): # конструктор класса
        pass

    def main(self): # функция для оценки модели
        config = ConfigurationManager() # получить конфигурацию
        model_evaluation_config = config.get_model_evaluation_config() # получить конфигурацию для оценки модели
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config) 
        # конфигурация для оценки модели
        model_evaluation_config.evaluate() # оценить модель