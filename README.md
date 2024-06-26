<h1 align="center">Palette</h1> 
  
 Основной стек проекта:
  
      1. Python==3.11
      
      2. Django==4.1.13

      4. Djangorestframework==3.15.1

      5. Djangorestframework-simplejwt==5.3.1

      6. Celery==5.3.6

      7. Redis==5.0.3
      
      8. PostgreSQL

<h2 align="left">Для запуска проекта необходимо:</h2>
  
• Установить виртуальное окружение в корневой папке проекта командой:
```shell
python3.11 -m venv venv
```

• Создать в корне проекта файл ```.env``` и заполнить данные по образцу из файла ```.env.sample```

• Установить все необходимые зависимости, указанные в файле ```requirements.txt```:
```shell
pip install -r requirements.txt
```
• Выполнить создание и применение миграций командами:
```shell
python manage.py makemigration
```
```shell
python manage.py migrate
```
   
• Создать суперпользователя командой:
```shell
python manage.py csu
```

• Запустить сервер командой
```shell
python manage.py runserver
```

• Запустить Celery командой:
```shell
celery -A config worker -l INFO
```

<h2 align="left">Для запуска проекта через Docker необходимо:</h2>

Создать и заполнить файл ```.env``` по шаблону файла ```.env.sample```

Создать и заполнить файл ```.env.docker``` по шаблону файла ```.env.docker.sample```

Создать Docker контейнер командой:
```shell
docker-compose build
```
Запустить Docker контейнер командой:
```shell
docker-compose up
```

    Для тестирования сервиса рекомендуется использовать ```Postman```

________________________________________
## Эндпоинты (Endpoints)

### Регистрация пользователя

URL: /users/sign-up/

Метод: ```POST```

Пример запроса:

{
    "email": "......",
    "password": "......"
}
________________________________________
### Авторизация пользователя

URL: /users/sign-in/

Метод: ```POST```

Пример запроса:

{
    "email": "......",
    "password": "......"
}

Ответ:

{
    "JWT Token": "......"
}
________________________________________
### Запрос на смену пароля

URL: /users/recovery/

Метод: ```POST```

Пример запроса:

{
    "email": "......"
}

Ответ:
- Получаем сообщение на почту с ссылкой на смену пароля
________________________________________
### Смена пароля

URL: /users/recovery/:hash/ - (ссылка отправленная на почту)

Метод: ```PATCH```

Пример запроса:

{
    "password": "......"
}  

Ответ:
- Смена пароля успешно выполнена
________________________________________
### Получение списка/создание палитр

URL: /palette/list-create/

Метод: ```GET```

Ответ:
- Выводит список палитр принадлжащих пользователю

Метод: ```POST```

Пример запроса:

{
    "name": "......"
}  

Ответ:
- Палитра создана
________________________________________
### Получение списка/изменение/удаление палитр

URL: /palette/list-update/<int:pk>/

Метод: ```GET```

Пример запроса:

Ответ:
- Выводит список палитр принадлжащих пользователю

Метод: ```PUT```

Пример запроса:

{
    "name": "......"
}  

Ответ:
- Палитра изменена

Метод: ```DELETE```

Ответ:
- Палитра удалена
________________________________________
### Получение списка/создание/ цветов

URL: /palette/color-list-create/<int:palette_id>/colors/

Метод: ```GET```

Ответ:
- Выводит список цветов принадлжащих палитре пользователя

Метод: ```POST```

Пример запроса:

{
    "palette": <int:palette_id>,
    "hex_code": "......"
} 

Ответ:
- Цвет создан
________________________________________
### Получение списка/изменение/удаление цветов

URL: /palette/color-list-update/<int:palette_id>/colors/<int:pk>/

Метод: ```GET```

Ответ:
- Выводит список цветов принадлжащих палитре пользователя

Метод: ```POST```

Пример запроса:

{
    "palette": <int:palette_id>,
    "hex_code": "......"
} 

Ответ:
- Цвет изменен

Метод: ```DELETE```

Ответ:
- Цвет удален
________________________________________
- К проекту подключен Swagger, дополнительную информацию можно найти там по URL: ```/docs/```

### Удачи!
