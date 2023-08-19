from dataclasses import dataclass # импорт декоратора для создания неизменяемого класса
from pathlib import Path # импорт класса для работы с путями

@dataclass(frozen=True) # декоратор для создания неизменяемого класса
class DataIngestionConfig: # класс для хранения конфигурации загрузки данных
    root_dir: Path # путь к корневой директории
    source_URL: str # URL источника данных
    local_data_file: Path # путь к локальному файлу с данными
    unzip_dir: Path # путь к директории для распаковки архива

@dataclass(frozen=True) # декоратор для создания неизменяемого класса
class DataValidationConfig: # класс для хранения конфигурации валидации данных
    root_dir: Path # путь к корневой директории
    STATUS_FILE: str # имя файла со статусом
    ALL_REQUIRED_FILES: list # список необходимых файлов

@dataclass(frozen=True) # декоратор для создания неизменяемого класса
class DataTransformationConfig: # класс для хранения конфигурации преобразования данных
    root_dir: Path # путь к корневой директории
    data_path: Path # путь к файлу с данными
    tokenizer_name: Path # путь к файлу с токенайзером