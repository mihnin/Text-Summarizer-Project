from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

@dataclass(frozen=True) # неизменяемый класс
class ModelTrainerConfig: # конфигурация для обучения модели
    root_dir: Path # корневая директория
    data_path: Path # путь к данным
    model_ckpt: Path # путь к чекпоинту модели
    num_train_epochs: int # количество эпох
    warmup_steps: int # количество шагов для прогрева
    per_device_train_batch_size: int # размер батча
    weight_decay: float # коэффициент регуляризации
    logging_steps: int # шаги логирования
    evaluation_strategy: str # стратегия оценки
    eval_steps: int # шаги оценки
    save_steps: float # шаги сохранения
    gradient_accumulation_steps: int # шаги накопления градиента
    

@dataclass(frozen=True) # неизменяемый класс
class ModelEvaluationConfig: # конфигурация для оценки модели
    root_dir: Path # корневая директория
    data_path: Path # путь к данным
    model_path: Path # путь к модели
    tokenizer_path: Path # путь к токенайзеру
    metric_file_name: Path # имя файла с метриками