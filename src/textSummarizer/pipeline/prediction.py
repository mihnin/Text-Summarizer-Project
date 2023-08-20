from textSummarizer.config.configuration import ConfigurationManager # импортируем класс конфигурации
from transformers import AutoTokenizer # импортируем токенайзер
from transformers import pipeline # импортируем пайплайн


class PredictionPipeline: # класс для предсказания
    def __init__(self): # конструктор класса
        self.config = ConfigurationManager().get_model_evaluation_config() # получаем конфигурацию


    
    def predict(self,text): # функция предсказания
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path) # получаем токенайзер
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128} # параметры для генерации

        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer) # получаем пайплайн

        print("Dialogue:") # выводим диалог
        print(text) # выводим текст

        output = pipe(text, **gen_kwargs)[0]["summary_text"] # получаем суммарный текст
        print("\nModel Summary:") # выводим суммарный текст
        print(output) # выводим суммарный текст

        return output # возвращаем суммарный текст