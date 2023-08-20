from transformers import AutoModelForSeq2SeqLM, AutoTokenizer # импортируем токенизатор и модель
from datasets import load_dataset, load_from_disk, load_metric # импортируем датасеты и метрики
import torch # импортируем torch
import pandas as pd # импортируем pandas
from tqdm import tqdm # импортируем tqdm
from textSummarizer.entity import ModelEvaluationConfig # импортируем конфигурацию для оценки модели


class ModelEvaluation: # класс для оценки модели
    def __init__(self, config: ModelEvaluationConfig): # конструктор класса
        self.config = config # конфигурация для оценки модели


    
    def generate_batch_sized_chunks(self,list_of_elements, batch_size): # функция для генерации батчей
        """split the dataset into smaller batches that we can process simultaneously 
        Yield successive batch-sized chunks from list_of_elements."""
        for i in range(0, len(list_of_elements), batch_size): # цикл по длине списка
            yield list_of_elements[i : i + batch_size] # возвращаем список элементов

    
    def calculate_metric_on_test_ds(self,dataset, metric, model, tokenizer, 
                               batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu", 
                               column_text="article", 
                               column_summary="highlights"): 
        # функция для вычисления метрики на тестовом датасете
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size)) 
        # разбиваем текст на батчи
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size)) 
        # разбиваем суммаризации на батчи

        for article_batch, target_batch in tqdm( 
            zip(article_batches, target_batches), total=len(article_batches)): # цикл по батчам
            
            inputs = tokenizer(article_batch, max_length=1024,  truncation=True, 
                            padding="max_length", return_tensors="pt") # токенизируем текст
            
            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                            attention_mask=inputs["attention_mask"].to(device), 
                            length_penalty=0.8, num_beams=8, max_length=128) # генерируем суммаризации
            ''' parameter for length penalty ensures that the model does not generate sequences that are too long. '''
            
            # Finally, we decode the generated texts, 
            # replace the  token, and add the decoded texts with the references to the metric.
            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, 
                                    clean_up_tokenization_spaces=True)  # декодируем суммаризации
                for s in summaries]      
            
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries] # заменяем токены
            
            
            metric.add_batch(predictions=decoded_summaries, references=target_batch) 
            # добавляем суммаризации и референсы в метрику
            
        #  Finally compute and return the ROUGE scores.
        score = metric.compute() # вычисляем метрику
        return score # возвращаем метрику


    def evaluate(self): # функция для оценки модели
        device = "cuda" if torch.cuda.is_available() else "cpu" # определяем устройство
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path) # загружаем токенизатор
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device) 
        # загружаем модель
       
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path) # загружаем данные


        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"] # инициализируем метрики
  
        rouge_metric = load_metric('rouge') # загружаем метрику

        score = self.calculate_metric_on_test_ds(
        dataset_samsum_pt['test'][0:10], rouge_metric, model_pegasus, tokenizer, 
        batch_size = 2, column_text = 'dialogue', column_summary= 'summary'
            ) # вычисляем метрику на тестовом датасете

        rouge_dict = dict((rn, score[rn].mid.fmeasure ) for rn in rouge_names ) # создаем словарь с метриками

        df = pd.DataFrame(rouge_dict, index = ['pegasus'] ) # создаем датафрейм с метриками
        df.to_csv(self.config.metric_file_name, index=False) # сохраняем датафрейм в файл