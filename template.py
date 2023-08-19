import os # импортируем модуль os
from pathlib import Path # импортируем класс Path
import logging # импортируем модуль логирования

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 
# настраиваем логирование


project_name = "textSummarizer" # имя проекта

list_of_files = [ # список файлов и директорий, которые необходимо создать
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files: # для каждого файла в списке файлов
    filepath = Path(filepath) # преобразуем путь к файлу в объект типа Path
    filedir, filename = os.path.split(filepath) # разделяем путь к файлу на путь к директории и имя файла

    if filedir != "": # если путь к директории не пустой
        os.makedirs(filedir, exist_ok=True) # создаем директорию
        logging.info(f"Creating directory:{filedir} for the file {filename}") # логируем создание 
        # директории

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # если файл не существует
        with open(filepath,'w') as f: # открываем файл на запись
            pass # ничего не делаем
            logging.info(f"Creating empty file: {filepath}") # логируем создание пустого файла


    
    else: # если файл существует
        logging.info(f"{filename} is already exists") # логируем, что файл уже существует