import asyncio
# import datetime
import json
from aiohttp import web

disable_endpoint = False


# Отдельнгая функция т.к маршрут принимает только 3 метода(тип запроса, путь,что должен вернуть)
async def handle_request(request):
    with open('config.json', 'r') as f:
        configs = json.load(f)
    for config in configs:
        if request.path == config['path']:
            if config['disable_endpoint'] == True:
                return web.Response(text='Эндпоинт отключен', status=404)
            await asyncio.sleep(config['duration'] / 1000)  # миллисекунды
            return web.json_response(json.loads(config['responseBody']))
    return web.Response(status=404)


# используем async т.к request.json() является асинхронным методом измерение в МС
async def update_duration(request):
    data = await request.json()
    with open('config.json', 'r') as f:
        configs = json.load(f)
    for config in configs:
        if config['path'] == data['path']:
            config['duration'] = data['duration']
    with open('config.json', 'w') as f:
        json.dump(configs, f)
    return web.Response(status=200)


# Функция отключения эндпоинта
async def off_endpoint(request):
    data = await request.json()
    with open('config.json', 'r') as f:
        configs = json.load(f)
    for config in configs:
        if config['path'] == data['path']:
            config['disable_endpoint'] = True
    with open('config.json', 'w') as f:
        json.dump(configs, f)
    web.Response(text='Эндпоинт отключен', status=200)
    await asyncio.sleep(data['duration_disable_endpoint'])  # ожидание указанного времени в секундах
    with open('config.json', 'r') as f:
        configs = json.load(f)
    for config in configs:
        if config['path'] == data['path']:
            config['disable_endpoint'] = False
    with open('config.json', 'w') as f:
        json.dump(configs, f)
    return web.Response(text='Эндпоинт включен', status=200)


app = web.Application()
app.router.add_route('POST', '/update_duration', update_duration)
app.router.add_route('POST', '/off_endpoint', off_endpoint)

# создание маршрутов исходя из файла конфига
with open('config.json', 'r') as f:
    configs = json.load(f)
for config in configs:
    app.router.add_route(config['method'], config['path'], handle_request)

# web.run_app(app, host='127.0.0.1', port=8000)
web.run_app(app, host='0.0.0.0', port=8000)
