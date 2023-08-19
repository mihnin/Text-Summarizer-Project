from dataclasses import dataclass # импорт декоратора для создания неизменяемого класса
from pathlib import Path # импорт класса для работы с путями

@dataclass(frozen=True) # декоратор для создания неизменяемого класса
class DataIngestionConfig: # класс для хранения конфигурации загрузки данных
    root_dir: Path # путь к корневой директории
    source_URL: str # URL источника данных
    local_data_file: Path # путь к локальному файлу с данными
    unzip_dir: Path # путь к директории для распаковки архива
