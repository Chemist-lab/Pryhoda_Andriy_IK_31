# **Лабораторна робота №3**
---
## Послідовність виконання лабораторної роботи:
#### 1. Створив папку ***lab3*** у власному репозиторію. Перейшовши у папку, проініціалізував середовище pipenv та встановив необхідні пакети за допомогою команд:
```bash
sudo pipenv --python 3.8
sudo pipenv install django
```
#### 2. За допомогою `Django Framework` створив заготовку (template) власного проекту `chemist_site`. Використовуючи команду `sudo pipenv run django-admin startproject chemist_site`. 
Для зручності виніс всі створені файли на один рівень вище щоб структура проекту була такою як показано нижче:
```bash
Lab3/
├── chemist_site/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
За допомогою команд:
```sh
sudo mv chemist_site/chemist_site/* chemist_site/
sudo mv chemist_site/manage.py ./
```
#### 3. Запускаю `Django` сервер. За допомогою команди `sudo pipenv run python manage.py runserver` та перейшов за посиланням яке вивелось у консолі.
Виконання команди в консолі:
```text
chemist@chemist-VirtualBox:~/tpis/Pryhoda_Andriy_IK_31/lab3$ pipenv run python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 05, 2021 - 18:26:11
Django version 3.2.9, using settings 'chemist_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
#### 4. Після того як все запустилось успішно і стартова сторінка `Django` відображається коректно, зупинив сервер виконавши переривання `Ctrl+C`. Створив коміт із базовим темплейтом сайту. А також ознайомився із функціоналом `Django Framework`.

#### 5. Далі створив темплейт свого додатку у якому буде описано всі web сторінки мого сайту `main`. За допомогою команди `sudo pipenv run python manage.py startapp main`. Також створив коміт із новоствореними файлами темплейту додатка.

#### 6. Cтворив папку `main/templates/`, а також у даній папці файл `main.html`. Також у папці додатку створив ще один файл `main/urls.py`. Зробив коміт із даними файлами.

#### 7. Після створення додатку вказав `Django frameworks` його назву та де шукати веб сторінки. Це здійснюється у файлі `my_site/settings.py` у змінній `INSTALLED_APPS`, а також вніс зміни у файл `site_lab3/urls.py
Доданий вміст до файлу `chemist_site/settings.py`:
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]
```
Доданий вміст до файлу `chemist_site/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```
#### 8. Далі переходжу до мого додатку та буду виконувати дії над WEB сторінками. Для цього: створив сторінки двох типів - перша буде зчитуватись з .html темплейта. друга сторінка буде просто повертати відповідь у форматі JSON.
Вміст файла `main/views.py`:
```py
from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime

def main(request):
    return render(request, 'main.html', {'parameter': "test"})

def health(request):
    response = {'date': 'test1', 'current_page': "test2", 'server_info': "test3", 'client_info': "test4"}
    return JsonResponse(response)
```
#### 9. Щоб поєднати функції із реальними URL шляхами за якими будуть доступні наші веб сторінки заповнив файл `main/urls.py` згідно зразка. Як можна зрозуміти з коду є два URL посилання:
* головна сторінка яка буде опрацьовуватись функцією main;
* сторінка health/ яка буде опрацьована функцією health;

Доданий вміст до файлу `main/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('health/', views.health, name='health')
]
```

#### 10. Запустив сервер та переконалався що сторінки доступні. Виконала коміт робочого `Django` сайту.
Виконання команди:
```text
chemist@chemist-VirtualBox:~/tpis/Pryhoda_Andriy_IK_31/lab3$
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 05, 2021 - 19:36:50
Django version 3.2.9, using settings 'site_lab3.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[05/Nov/2021 20:59:42] "GET /health HTTP/1.1" 301 0
[05/Nov/2021 20:59:42] "GET /health/ HTTP/1.1" 200 307
[05/Nov/2021 20:59:52] "GET /health/ HTTP/1.1" 200 361
[05/Nov/2021 20:59:53] "GET /health/ HTTP/1.1" 200 361
[05/Nov/2021 20:59:54] "GET /health/ HTTP/1.1" 200 361
[05/Nov/2021 20:59:54] "GET /health/ HTTP/1.1" 200 361
Not Found: /heal
[05/Nov/2021 20:59:56] "GET /heal HTTP/1.1" 404 2424
Not Found: /heal
[05/Nov/2021 20:59:57] "GET /heal HTTP/1.1" 404 2424
[05/Nov/2021 20:59:59] "GET /health/ HTTP/1.1" 200 361
Not Found: /favicon.ico
```
#### 11. Роль моніторингу буде здійснювати файл `monitoring.py` який за допомогою бібліотеки `requests` буде опитувати сторінку `health`. Встановлюємо дану бібліотеку;
     ```bash
     pipenv install requests
     ```
     
#### 12. Як видно із заготовленої функції health() відповідь формується як Пайтон словник і далі обробляється функцією JsonResponse(). 

#### 13. Здача/захист лабораторної:
     1. модифікувати функцію `health` так щоб у відповіді були: згенерована на сервері дата, URL сторінки моніторингу, інформація про сервер на якому запущений сайт та інформація про клієнта який робить запит до сервера;
    ```bash
     def health(request):
    osInfo = os.uname()
    response = {
    'date': datetime.now().strftime("%d.%m.%y %H:%M"),
    'current_page': request.get_host() + request.get_full_path(),
    'server_info': f"OSName: {osInfo.sysname}; NodeName: {osInfo.nodename}; Release:{osInfo.release}; Version:{osInfo.version}; Indentificator:{osInfo.machine}",
    'client_info': f"Browser: {request.META['HTTP_USER_AGENT']}  IP: {request.META['REMOTE_ADDR']} "
    }
    return JsonResponse(response)
    ```
     2. дописати функціонал який буде виводити повідомлення про недоступність сайту у випадку якщо WEB сторінка недоступна 
    ```bash
     try:
         r = requests.get(url)
         data = json.loads(r.content)
         logging.info("Сервер доступний. Час на сервері: %s", data['date'])
         logging.info("Запитувана сторінка: : %s", data['current_page'])
         logging.info("Відповідь сервера місти наступні поля:")
         for key in data.keys():
              logging.info("Ключ: %s, Значення: %s", key, data[key])
    except Exception as x:
         logging.error("Сервер недоступний.")
    ``` 
     3. після запуску моніторингу запит йде лише один раз після чого програма закінчується - зробіть так щоб дана програма запускалась раз в хвилину та працювала в бекграунді (період запуску зробити через функціонал мови Python);
    ```bash
     while(True):
        main("http://localhost:8000/health")
        time.sleep(60)
     ``` 
       Для запуску в беграунді викликаємо файл так
    ```bash
     pipenv run python3 monitoring.py &
     ``` 
     4. спростіть роботу з пайтон середовищем через швидкий виклик довгих команд, для цього зверніть увагу на секцію `scripts` у Pipfile. Зробіть аліас на запус моніторингу:
         ```bash
         pipenv run mon
         ```
        ```bash
        [scripts]
        server = "python manage.py runserver"
        mon = "python3 monitoring.py"
        ```
#### 14.Переконуємося що все працює, комітимо `server.logs` . 

#### 15.Після успішного виконання роботи редагуємо  README.md у цьому репозиторію.
