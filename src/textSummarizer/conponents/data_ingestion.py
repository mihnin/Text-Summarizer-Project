import os # импортируем модуль os для работы с файловой системой
import urllib.request as request # импортируем модуль request для загрузки файлов по URL
import zipfile # импортируем модуль zipfile для работы с архивами
from textSummarizer.logging import logger # импортируем логгер
from textSummarizer.utils.common import get_size # импортируем функцию для получения размера файла
from pathlib import Path # импортируем класс для работы с путями
from textSummarizer.entity import DataIngestionConfig 
# импортируем класс DataIngestionConfig из модуля entity


class DataIngestion: # класс для загрузки данных
    def __init__(self, config: DataIngestionConfig): # конструктор класса
        self.config = config # сохраняем конфигурацию загрузки данных в переменную config


    
    def download_file(self): # метод для загрузки файла
        if not os.path.exists(self.config.local_data_file): # если файл не существует
            filename, headers = request.urlretrieve( # загружаем файл
                url = self.config.source_URL, # по URL из конфигурации
                filename = self.config.local_data_file # сохраняем файл по пути из конфигурации
            )
            logger.info(f"{filename} download! with following info: \n{headers}") 
            # логируем, что файл загружен
        else: # если файл существует
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}") 
            # логируем, что файл уже существует 

        
    
    def extract_zip_file(self): # метод для распаковки архива
        """
        # путь к zip файлу
        # распаковывает zip файл в директорию data
        # функция ничего не возвращает
        """
        unzip_path = self.config.unzip_dir # получаем путь к директории для распаковки из конфигурации
        os.makedirs(unzip_path, exist_ok=True) # создаем директорию для распаковки
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref: # открываем архив
            zip_ref.extractall(unzip_path) # распаковываем архив