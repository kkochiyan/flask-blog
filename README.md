# Flask Blog

Простой и удобный блог на Flask для публикации статей и новостей.

## Функциональности

-  Создание, редактирование и удаление статей
-  Поиск по заголовкам статей
-  Просмотр всех статей на отдельной странице
-  Главная страница с топом свежих статей
-  Адаптивный дизайн (Bootstrap 5)
-  База данных SQLite

## Технологии

- **Backend:** Flask, Flask-SQLAlchemy
- **Frontend:** Bootstrap 5, Jinja2
- **Database:** SQLite
- **Python:** 3.13

## Установка и запуск

1. **Клонируйте репозиторий:**
```
git clone <your-repo-url>
cd FlaskBlog
```

2. **Создайте виртуальное окружение:**
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows
```

3. **Установите зависимости:**
```
pip install -r requirements.txt
```

4. **Инициализируйте базу данных:**
```
python create_db.py
```

5. **Запустите приложение:**
```
python run.py
```

6. **Откройте в браузере**
```
http://localhost:5000
```