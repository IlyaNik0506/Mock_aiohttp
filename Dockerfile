# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в рабочую директорию контейнера
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install aiohttp

# Проброс порта 8000 из контейнера на хост-машину
EXPOSE 8000

# Запускаем приложение
CMD ["python", "main.py"]
