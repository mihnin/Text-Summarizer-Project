
from textSummarizer.constants import * # импортируем все константы из модуля constants
from textSummarizer.utils.common import read_yaml, create_directories 
# new path
from textSummarizer.entity import (DataIngestionConfig) 
# импортируем класс DataIngestionConfig из модуля entity

class ConfigurationManager: # создаем класс ConfigurationManager
    def __init__( # конструктор класса
        self, # ссылка на текущий объект
        config_filepath = CONFIG_FILE_PATH, # путь к файлу конфигурации
        params_filepath = PARAMS_FILE_PATH): # путь к файлу параметров
        self.config = read_yaml(config_filepath) # сохраняем конфигурацию в переменную config
        self.params = read_yaml(params_filepath) # сохраняем параметры в переменную params
        
        create_directories([self.config.artifacts_root]) # создаем директорию для артефактов
        
    def get_data_ingestion_config(self) -> DataIngestionConfig: 
        # метод для получения конфигурации загрузки данных
        config = self.config.data_ingestion # получаем конфигурацию загрузки данных

        create_directories([config.root_dir]) # создаем директорию для загрузки данных

        return DataIngestionConfig( # возвращаем конфигурацию загрузки данных
            root_dir=config.root_dir, # путь к корневой директории
            source_URL=config.source_URL, # URL источника данных
            local_data_file=config.local_data_file, # путь к локальному файлу с данными
            unzip_dir=config.unzip_dir, # путь к директории для распаковки архива
        )
