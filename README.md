# Поиск в интернете

Небольшое Flask‑приложение для поиска по DuckDuckGo и парсинга первых фрагментов текста с найденных страниц.

## 📦 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd <директория_проекта>

2. Создайте и активируйте виртуальное окружение:
  ``bash
  python3 -m venv venv
  source venv/bin/activate      # Linux/macOS
  venv\Scripts\activate.bat     # Windows

3. Установите зависимости:
  ```bash
  pip install -r requirements.txt

## ⚙️ Конфигурация
Создайте файл .env (не коммитить в Git!) и при необходимости задайте:

  ```bash
  FLASK_ENV=development
  SEARCH_LIMIT=5
  EXCERPT_MAX_CHARS=300
  REQUEST_TIMEOUT=5
  CACHE_TTL=21600        # в секундах (6 часов)


## 🚀 Запуск


  ``bash
  export FLASK_APP=app.py
  export FLASK_ENV=development    # или production
  flask run
По умолчанию приложение будет доступно по адресу http://127.0.0.1:5000/

## 📝 Использование

Откройте в браузере http://127.0.0.1:5000/

Введите поисковую фразу и нажмите Искать

Просматривайте результаты в виде карточек с заголовком, фрагментом текста и ссылкой.

## 🛠️ Тестирование
  ```bash
  pytest
