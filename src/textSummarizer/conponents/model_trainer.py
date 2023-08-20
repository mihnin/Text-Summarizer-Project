from transformers import TrainingArguments, Trainer # импортировать классы для обучения модели
from transformers import DataCollatorForSeq2Seq # импортировать класс для обработки данных
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer # импортировать классы для работы с моделью
from datasets import load_dataset, load_from_disk # импортировать классы для работы с датасетом
from textSummarizer.entity import ModelTrainerConfig # импортировать конфигурацию для обучения модели
import torch # импортировать библиотеку для работы с тензорами
import os # импортировать библиотеку для работы с файлами


class ModelTrainer: # класс для обучения модели
    def __init__(self, config: ModelTrainerConfig): # конструктор класса
        self.config = config # конфигурация для обучения модели


    
    def train(self): # метод для обучения модели
        device = "cuda" if torch.cuda.is_available() else "cpu" # определить устройство для обучения модели
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt) # загрузить токенайзер
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device) 
        # загрузить модель
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus) 
        # создать объект для обработки данных
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path) # загрузить датасет
        
        # trainer_args = TrainingArguments( # создать объект для обучения модели
        #     output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, 
        #     warmup_steps=self.config.warmup_steps,
        #     per_device_train_batch_size=self.config.per_device_train_batch_size, 
        #     per_device_eval_batch_size=self.config.per_device_train_batch_size,
        #     weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
        #     evaluation_strategy=self.config.evaluation_strategy, 
        #     eval_steps=self.config.eval_steps, save_steps=1e6,
        #     gradient_accumulation_steps=self.config.gradient_accumulation_steps
        # ) 


        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        ) 

        trainer = Trainer(model=model_pegasus, args=trainer_args, # создать объект для обучения модели
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator, # создать объект для обработки данных
                  train_dataset=dataset_samsum_pt["test"],  # загрузить датасет для обучения модели
                  eval_dataset=dataset_samsum_pt["validation"]) # загрузить датасет для валидации модели
        
        trainer.train() # обучить модель

        ## Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model")) 
        # сохранить модель
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer")) 
        # сохранить токенайзер
        