from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
<<<<<<< HEAD
# Импортируем класс DataIngestionTrainingPipeline из модуля stage_01_data_ingestion 
# в пакете pipeline в проекте textSummarizer

from textSummarizer.logging import logger
# Импортируем объект logger из модуля logging в проекте textSummarizer
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline 
# Импортируем класс DataValidationTrainingPipeline из модуля stage_02_data_validation 
# в пакете pipeline в проекте textSummarizer

from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
# Создаем константу STAGE_NAME со значением "Data Ingestion stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   # Логируем информационное сообщение о начале выполнения этапа с помощью объекта logger

   data_ingestion = DataIngestionTrainingPipeline()
   # Создаем экземпляр класса DataIngestionTrainingPipeline и присваиваем его переменной data_ingestion

   data_ingestion.main()
   # Вызываем метод main() у объекта data_ingestion

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   # Логируем информационное сообщение об успешном завершении выполнения этапа с помощью объекта logger
except Exception as e:
        logger.exception(e)
        # Логируем ошибку с помощью объекта logger
        raise e
        # Выбрасываем исключение, чтобы прервать выполнение программы

STAGE_NAME = "Data Validation stage" # создаем константу STAGE_NAME со значением "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  
   # логируем информационное сообщение о начале выполнения этапа с помощью объекта logger
   data_validation = DataValidationTrainingPipeline() 
   # создаем экземпляр класса DataValidationTrainingPipeline и присваиваем его переменной data_validation
   data_validation.main() 
   # вызываем метод main() у объекта data_validation
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x") 
   # логируем информационное сообщение об успешном завершении выполнения этапа с помощью объекта logger
except Exception as e: # обрабатываем исключение
        logger.exception(e) # логируем ошибку с помощью объекта logger
        raise e # выбрасываем исключение, чтобы прервать выполнение программы

STAGE_NAME = "Data Transformation stage" # создаем константу STAGE_NAME со значением "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  
   # логируем информационное сообщение о начале выполнения этапа с помощью объекта logger
   data_transformation = DataTransformationTrainingPipeline() 
   # создаем экземпляр класса DataTransformationTrainingPipeline и присваиваем его переменной data_transformation
   data_transformation.main() 
   # вызываем метод main() у объекта data_transformation
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x") 
   # логируем информационное сообщение об успешном завершении выполнения этапа с помощью объекта logger
except Exception as e: # обрабатываем исключение
        logger.exception(e) # логируем ошибку с помощью объекта logger
        raise e # выбрасываем исключение, чтобы прервать выполнение программы
=======

from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
>>>>>>> d021832c63440171a1a0531580f3a4685fbe0f71
