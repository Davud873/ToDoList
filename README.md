# ToDoList API на Django REST Framework с JWT

API для управления списком задач, разработанное с использованием Python, фреймворка Django и Django REST Framework для создания RESTful API. Для аутентификации используется JSON Web Tokens (JWT).

## Описание

Это API предоставляет набор эндпоинтов для управления списком задач. Пользователи могут регистрироваться, аутентифицироваться и выполнять CRUD-операции (создание, чтение, обновление, удаление) над задачами, принадлежащими их учетной записи. Безопасность API обеспечивается с помощью JWT-аутентификации.

## Технологии

* Python
* Django
* Django REST Framework
* djangorestframework-simplejwt

## Установка

1.  Клонируйте репозиторий:
    ```bash
    git clone <URL вашего репозитория>
    cd todolist
    ```

2.  Создайте и активируйте виртуальное окружение (рекомендуется):
    **Для Linux/macOS:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
    **Для Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4.  Выполните миграции базы данных:
    ```bash
    python manage.py migrate
    ```

5.  Создайте суперпользователя (для доступа к административной панели Django и тестирования):
    ```bash
    python manage.py createsuperuser
    ```

6.  Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

    API будет доступен по адресу `http://127.0.0.1:8000/api/`.

## API Эндпоинты

**Аутентификация**

* **POST /api/token/:** Получение пары токенов (access и refresh) по логину и паролю.
    **Запрос:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
    **Ответ:**
    ```json
    {
        "access": "...",
        "refresh": "..."
    }
    ```

* **POST /api/token/refresh/:** Обновление access токена с помощью refresh токена.
    **Запрос:**
    ```json
    {
        "refresh": "your_refresh_token"
    }
    ```
    **Ответ:**
    ```json
    {
        "access": "..."
    }
    ```

**Задачи**

* **GET /api/tasks/:** Получение списка всех задач текущего пользователя.
    **Требуется:** JWT access токен в заголовке `Authorization: Bearer <your_access_token>`.

* **POST /api/tasks/:** Создание новой задачи.
    **Требуется:** JWT access токен в заголовке `Authorization: Bearer <your_access_token>`.
    **Запрос:**
    ```json
    {
        "title": "Название задачи",
        "description": "Описание задачи (опционально)",
        "completed": false,
        "priority": "low" или "medium" или "high" (опционально, по умолчанию "medium"),
        "deadline": "YYYY-MM-DDTHH:MM:SSZ" (опционально)
    }
    ```


## Использование API

Для взаимодействия с API вам потребуется отправлять HTTP-запросы (например, с помощью `curl`, `Postman` или вашего любимого HTTP-клиента). Большинство защищенных эндпоинтов требуют передачи JWT access токена в заголовке `Authorization` в формате `Bearer <your_access_token>`.

1.  Получите JWT токены, отправив `POST` запрос на `/api/token/` с вашими учетными данными.
2.  Используйте полученный `access` токен для доступа к защищенным эндпоинтам, передавая его в заголовке `Authorization`.
