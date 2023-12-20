ЗАГЛУШКА

Для конкретного запроса изменение времени отклика
curl -X POST -H "Content-Type: application/json" -d "{"path": "/issuing/pin/counter", "duration": 500}"http://127.0.0.1:8000/update_duration

Для всех запросов сразу (не работает, нужно создать отдельный маршрут для обработки сразу всех эндпоинтов)
curl -X POST -H "Content-Type: application/json" -d "{"duration": 100}" http://127.0.0.1:8000/update_duration

Отключение эндпоинта (в секундах)
curl -X POST -H "Content-Type: application/json" -d '{"path": "/issuing/pin/counter", "duration_disable_endpoint": 5}' http://localhost:8000/off_endpoint

Команды для запуска Dockerfile 
docker build -t aiohttp .   - сборка контейнера 
docker images - все образы 
docker tag 3b00077e80f0 aiohttp:latest - переименование образа с тегом
docker run -it -p 8000:8000 aiohttp  - запуск

Важное замечание  не стоит перезаписывать файл в момент перезаписи файла )))))) Т.к может возникнуть	 проблема т.к все функции выполняются асинхронно (будет гонка функций)
