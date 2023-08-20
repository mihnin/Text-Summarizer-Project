from fastapi import FastAPI # импортируем библиотеку FastAPI для создания API
import uvicorn # импортируем библиотеку uvicorn для запуска сервера
import sys # импортируем библиотеку sys для работы с системными параметрами
import os  # импортируем библиотеку os для работы с файловой системой
from fastapi.templating import Jinja2Templates # импортируем библиотеку Jinja2Templates для работы с шаблонами
from starlette.responses import RedirectResponse # импортируем библиотеку RedirectResponse для редиректа
from fastapi.responses import Response # импортируем библиотеку Response для работы с ответами
from textSummarizer.pipeline.prediction import PredictionPipeline 
# импортируем класс PredictionPipeline для предсказания


text:str = "What is Text Summarization?" # текст для предсказания

app = FastAPI() # создаем экземпляр класса FastAPI

@app.get("/", tags=["authentication"]) # создаем корневой маршрут
async def index(): # функция для корневого маршрута
    return RedirectResponse(url="/docs") # редирект на документацию



@app.get("/train") # создаем маршрут для обучения
async def training(): # функция для обучения
    try: # обрабатываем исключения
        os.system("python main.py") # запускаем обучение
        return Response("Training successful !!") # возвращаем ответ

    except Exception as e: # обрабатываем исключения
        return Response(f"Error Occurred! {e}") # возвращаем ответ
    



@app.post("/predict") # создаем маршрут для предсказания
async def predict_route(text): # функция для предсказания
    try: # обрабатываем исключения

        obj = PredictionPipeline() # создаем экземпляр класса PredictionPipeline
        text = obj.predict(text) # получаем суммарный текст
        return text # возвращаем суммарный текст
    except Exception as e: # обрабатываем исключения
        raise e # возвращаем исключение
    

if __name__=="__main__": # если файл запускается как главный
    uvicorn.run(app, host="0.0.0.0", port=7777) # запускаем сервер