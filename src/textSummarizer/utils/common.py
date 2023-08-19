import os  # импортируем модуль os
from box.exceptions import BoxValueError  # импортируем исключение BoxValueError
import yaml  # импортируем модуль для работы с YAML файлами
from textSummarizer.logging import logger  # импортируем объект logger из модуля logging
from ensure import ensure_annotations  # импортируем декоратор ensure_annotations
from box import ConfigBox  # импортируем класс ConfigBox из модуля box
from pathlib import Path  # импортируем класс Path
from typing import Any  # импортируем класс Any для аннотации типов


@ensure_annotations # декоратор для проверки типов аргументов и возвращаемого значения
def read_yaml(path_to_yaml: Path) -> ConfigBox: # функция для чтения YAML файлов
    """reads yaml file and returns

    Args:
        path_to_yaml (Path): путь к YAML файлу

    Raises:
        ValueError: если YAML файл пустой
        e: пустой файл

    Returns:
        ConfigBox: объект типа ConfigBox
    """
    try:
        with open(path_to_yaml) as yaml_file:  # открываем YAML файл
            content = yaml.safe_load(yaml_file)  # загружаем содержимое YAML файла
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # логируем 
            # успешную загрузку YAML файла
            return ConfigBox(content)  # возвращаем объект типа ConfigBox
    except BoxValueError:  # если YAML файл пустой
        raise ValueError("yaml file is empty")  # вызываем исключение ValueError
    except Exception as e:  # если возникла какая-то другая ошибка
        raise e  # вызываем исключение


@ensure_annotations # декоратор для проверки типов аргументов и возвращаемого значения
def create_directories(path_to_directories: list, verbose=True): # функция для создания директорий
    """create list of directories

    Args:
        path_to_directories (list): список путей к директориям
        verbose (bool, optional): выводить информацию о создании директорий. По умолчанию True.
    """
    for path in path_to_directories:  # для каждого пути в списке путей
        os.makedirs(path, exist_ok=True)  # создаем директорию
        if verbose:  # если verbose=True
            logger.info(f"created directory at: {path}")  # логируем создание директории


@ensure_annotations # декоратор для проверки типов аргументов и возвращаемого значения
def get_size(path: Path) -> str: # функция для получения размера файла
    """get size in KB

    Args:
        path (Path): путь к файлу

    Returns:
        str: размер файла в КБ
    """
    size_in_kb = round(os.path.getsize(path)/1024)  # вычисляем размер файла в КБ
    return f"~ {size_in_kb} KB"  # возвращаем размер файла в КБ в виде строки
