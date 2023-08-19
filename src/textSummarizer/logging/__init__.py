import os # импортируем модуль os
import sys # импортируем модуль sys
import logging # импортируем модуль логирования

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 
# строка формата для логирования
log_dir = "logs" # путь к директории с логами
log_filepath = os.path.join(log_dir,"running_logs.log") # путь к файлу с логами
os.makedirs(log_dir, exist_ok=True) # создаем директорию с логами



logging.basicConfig( # настраиваем логирование
    level= logging.INFO, # уровень логирования
    format= logging_str, # строка формата

    handlers=[ # обработчики логов
        logging.FileHandler(log_filepath), # обработчик для записи логов в файл
        logging.StreamHandler(sys.stdout) # обработчик для вывода логов в консоль
    ]
)

logger = logging.getLogger("textSummarizerLogger") # создаем объект логирования
