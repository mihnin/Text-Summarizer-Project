import os # импортируем библиотеку для работы с файловой системой
from textSummarizer.logging import logger # импортируем логгер
from transformers import AutoTokenizer # импортируем токенизатор
from datasets import load_dataset, load_from_disk # импортируем методы для загрузки датасета
from textSummarizer.entity import DataTransformationConfig 
# импортируем класс конфигурации преобразования данных



class DataTransformation: # создаем класс DataTransformation
    def __init__(self, config: DataTransformationConfig): # конструктор класса
        self.config = config # сохраняем конфигурацию в переменную config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name) 
        # инициализируем токенизатор


    
    def convert_examples_to_features(self,example_batch): # метод для преобразования данных
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True ) 
        # токенизируем диалог
        
        with self.tokenizer.as_target_tokenizer(): # используем токенизатор для целевых данных
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True ) 
            # токенизируем суммарный текст
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        } # возвращаем словарь с токенизированными данными
    

    def convert(self): # метод для преобразования данных
        dataset_samsum = load_from_disk(self.config.data_path) # загружаем датасет
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True) 
        # преобразуем данные
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset")) 
        # сохраняем датасет