from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# Импортируем класс DataIngestionTrainingPipeline из модуля stage_01_data_ingestion 
# в пакете pipeline в проекте textSummarizer

from textSummarizer.logging import logger
# Импортируем объект logger из модуля logging в проекте textSummarizer

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
