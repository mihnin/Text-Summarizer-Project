import setuptools # импортируем пакет setuptools

with open("README.md", "r", encoding="utf-8") as f: # открываем файл README.md
     long_description = f.read() # читаем файл README.md


__version__ = "0.0.0" # создаем константу __version__ со значением "0.0.0"

REPO_NAME = "project_1" # создаем константу REPO_NAME со значением "project_1" 
AUTHOR_USER_NAME = "mihnin" # создаем константу AUTHOR_USER_NAME со значением "mihnin"
SRC_REPO = "textSummarizer" # создаем константу SRC_REPO со значением "textSummarizer"
AUTHOR_EMAIL = "mihnin@gmail.com" # создаем константу AUTHOR_EMAIL со значением "



setuptools.setup( # вызываем функцию setup() из пакета setuptools
    name=SRC_REPO, # указываем имя пакета
    version=__version__, # указываем версию пакета
    author=AUTHOR_USER_NAME, # указываем автора пакета
    author_email=AUTHOR_EMAIL, # указываем автора пакета
    description="A small python package for NLP app", # описание пакета
    long_description=long_description, # длинное описание пакета
    long_description_content="text/markdown", # тип контента
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", # ссылка на репозиторий
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", 
        # ссылка на багтрекер
    },
    package_dir={"": "src"}, # указываем, что все модули находятся в папке src
    packages=setuptools.find_packages(where="src") # указываем, что все модули находятся в папке src
) # указываем параметры функции setup()