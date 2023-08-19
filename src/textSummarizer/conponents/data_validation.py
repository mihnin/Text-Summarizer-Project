import os # импортируем модуль os для работы с файлами и папками
from textSummarizer.logging import logger # импортируем логгер
from textSummarizer.entity import DataValidationConfig 
# импортируем класс DataValidationConfig из модуля entity

class DataValiadtion: # создаем класс DataValiadtion
    def __init__(self, config: DataValidationConfig): # конструктор класса
        self.config = config # сохраняем конфигурацию в переменную config


    
    def validate_all_files_exist(self)-> bool: # метод для проверки наличия всех необходимых файлов
        try:
            validation_status = None # инициализируем переменную для хранения статуса валидации

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset")) 
            # получаем список всех файлов в директории

            for file in all_files: # проходим по всем файлам
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False # статус валидации - False
                    with open(self.config.STATUS_FILE, 'w') as f: # записываем статус в файл
                        f.write(f"Validation status: {validation_status}") 
                else:
                    validation_status = True # статус валидации - True
                    with open(self.config.STATUS_FILE, 'w') as f: # записываем статус в файл
                        f.write(f"Validation status: {validation_status}") # записываем статус в файл

            return validation_status # возвращаем статус валидации
        
        except Exception as e: # если возникла ошибка
            raise e # выбрасываем исключение