# **Лабораторна робота №4**
---
## Послідовність виконання лабораторної роботи:
#### 1. Для ознайомляння з `Docker` звернувся до документації.
#### 2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустітив перевірку версії командою `sudo docker -v > my_work.log`, виведення допомоги командою `sudo docker --help >> my_work.log` та тестовий імедж командою `sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log`. Вивід цих команд перенаправляв у файл `my_work.log` та закомітив його до репозиторію.
#### 3. `Docker` працює з Імеджами та Контейнерами. Імедж це свого роду операційна система з попередньо інстальованим ПЗ. Контейнер це запущений Імедж. Ідея роботи `Docker` дещо схожа на віртуальні машини. Спочатку створив імедж з якого буде запускатись контейнер.
#### 4. Для знайомства з `Docker` створив імедж із `Django` сайтом зробленим у попередній роботі.
1. ##### Оскільки мій проект на `Python` то і базовий імедж також потрібно вибрати відповідний. Використовую команду `docker pull python:3.8-slim` щоб завантажити базовий імедж з репозиторію. Переглядаю створеного вміст імеджа командою `docker inspect python:3.8-slim`
    ##### Перевіряю чи добре встановився даний імедж командою:
    
    ```text
    chemist@chemist-VirtualBox:~/tpis/Pryhoda_Andriy_IK_31/lab4$ sudo docker images
    REPOSITORY        TAG        IMAGE ID       CREATED       SIZE
    python            3.8-slim   214d62795dbb   2 weeks ago   122MB
    docker/whalesay   latest     6b362a9f73eb   6 years ago   247MB
    ```
2. ##### Створив файл з іменем `Dockerfile` та скопіював туди вміс такого ж файлу з репозиторію викладача.
    ###### Вміст файлу `Dockerfile`:
    ```text
    FROM python:3.8-slim
    
    LABEL author="Bohdan"
    LABEL version=1.0
    
    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y
    
    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv
    
    # Створюємо робочу папку
    WORKDIR /lab
    
    # Завантажуємо файли з Git
    RUN git clone https://github.com/BobasB/devops_course.git
    
    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/devops_course/lab3/* .
    
    # Інсталюємо всі залежності
    RUN pipenv install
    
    # Відкриваємо порт 8000 на зовні
    EXPOSE 8000
    
    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
3. ##### Ознайомився із коментарями та зрозумів структуру написання `Dockerfile`.
4. ##### Змінений`Dockerfile` файл:
    ```text
    FROM python:3.8-slim

    LABEL author="myname"
    LABEL version=1.0
    
    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y
    
    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv
    
    # Створюємо робочу папку
    WORKDIR /lab
    
    # Завантажуємо файли з Git
    RUN git clone https://github.com/Chemist-lab/Pryhoda_Andriy_IK_31.git
    
    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/Pryhoda_Andriy_IK_31/lab3/* .
    
    # Інсталюємо всі залежності
    RUN pipenv install
    
    # Відкриваємо порт 8000 на зовні
    EXPOSE 8000
    
    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
#### 5. Створив власний репозиторій на [Docker Hub](https://hub.docker.com/repository/docker/chemist1337/lab4). Для цього залогінився у власний аккаунт на `Docker Hub` після чого перейшов у вкладку Repositories і далі натиснув кнопку `Create new repository`.
#### 6. Виконав білд (build) Docker імеджа та завантажтажив його до репозиторію. Для цього я повинен вказати правильну назву репозиторію та TAG. Оскільки мій репозиторій `chemist1337/lab4` то команда буде виглядати `sudo docker build -t chemist1337/lab4:django -f Dockerfile .`, де `django` - це тег.
Команда `docker images`:
```text
    chemist@chemist-VirtualBox:~/tpis/Pryhoda_Andriy_IK_31/lab4$ sudo docker images
    REPOSITORY         TAG        IMAGE ID       CREATED              SIZE
    chemist1337/lab4   django     7e4fc17080c4   About a minute ago   298MB
    python             3.8-slim   214d62795dbb   2 weeks ago          122MB
    docker/whalesay    latest     6b362a9f73eb   6 years ago          247MB
```
Команда для завантаження на власний репозеторій `docker push chemist1337/lab4:django`.
Посилання на мій [`Docker Hub`](https://hub.docker.com/repository/docker/chemist1337/lab4) репозиторій та посилання на [`імедж`](https://hub.docker.com/layers/177284460/chemist1337/lab4/django/images/sha256-aae55943e2bf91515df8ab14306b40caefa06d5695c7500b615becea2edfa7ac?context=repo).
#### 7. Для запуску веб-сайту виконав команду `sudo docker run -it --name=django --rm -p 8000:8000 chemist1337/lab4:django`:
```text
    sudo docker run -it --name=django --rm -p 8000:8000 chemist1337/lab4:django
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth,  contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    November 14, 2021 - 19:33:35
    Django version 3.2.9, using settings 'chemist_site.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.
```
Перейшов на адресу http://127.0.0.1:8000 та переконався що мій веб-сайт працює:
#### 8. Оскільки веб-сайт готовий і працює, потрібно створит ще один контейнер із програмою моніторингу нашого веб-сайту (Моє Завдання на роботу):
1. ##### Створив ще один Dockerfile з назвою `Dockerfile.site` в якому помістив програму моніторингу.
    Вміст файлу `Dockerfile.site`:
    ```text
    FROM python:3.8-slim

    LABEL author="myname2"
    LABEL version=1.0
    
    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y
    
    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv && pip install django
    
    # Створюємо робочу папку
    WORKDIR /lab
    
    # Завантажуємо файли з Git
    RUN git clone https://github.com/Chemist-lab/Pryhoda_Andriy_IK_31.git
    
    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/Pryhoda_Andriy_IK_31/lab3/* .
    
    # Інсталюємо всі залежності
    RUN pipenv install
    
    # Відкриваємо порт 8000 на зовні
    EXPOSE 8000
    
    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "monitoring.py", "0.0.0.0:8000"]
    ```
2. ##### Виконав білд даного імеджа та дав йому тег `monitoring` командами:
    ```text
    sudo docker build -f Dockerfile.site -t chemist1337/lab4:monitoring .
    docker push chemist1337/lab4:monitoring
    ```
3. ##### Запустив два контейнери одночасно (у різних вкладках) та переконався що програма моніторингу успішно доступається до сторінок мого веб-сайту.
    ##### Використовуючи команди:
    Запуск серевера:
    ```text
    sudo docker run -it --name=django --rm -p 8000:8000 chemist1337/lab4:django
    [sudo] password for chemist: 
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth,  contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    November 14, 2021 - 20:35:58
    Django version 3.2.9, using settings 'chemist_site.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.
    [14/Nov/2021 20:38:32] "GET /health HTTP/1.1" 301 0
    [14/Nov/2021 20:38:32] "GET /health/ HTTP/1.1" 200 302
    [14/Nov/2021 20:39:05] "GET / HTTP/1.1" 200 167
    [14/Nov/2021 20:39:07] "GET / HTTP/1.1" 200 167
    [14/Nov/2021 20:39:07] "GET / HTTP/1.1" 200 167
    [14/Nov/2021 20:39:07] "GET / HTTP/1.1" 200 167
    [14/Nov/2021 20:39:08] "GET / HTTP/1.1" 200 167
    [14/Nov/2021 20:39:09] "GET / HTTP/1.1" 200 167
    [14/Nov/2021 20:39:32] "GET /health HTTP/1.1" 301 0
    [14/Nov/2021 20:39:32] "GET /health/ HTTP/1.1" 200 302
    ```
    (перед запуском моніторингу спочатку створив файл server.log)
    Вміст файла `Server.log`:
    ```text
     INFO 2021-11-14 20:38:32,400 root : Сервер доступний. Час на сервері: 14.11.21 20:38
    INFO 2021-11-14 20:38:32,401 root : Запитувана сторінка: : localhost:8000/health/
    INFO 2021-11-14 20:38:32,401 root : Відповідь сервера місти наступні поля:
    INFO 2021-11-14 20:38:32,401 root : Ключ: date, Значення: 14.11.21 20:38
    INFO 2021-11-14 20:38:32,401 root : Ключ: current_page, Значення: localhost:8000/health/
    INFO 2021-11-14 20:38:32,401 root : Ключ: server_info, Значення: OSName: Linux; NodeName: b5650a934aea; Release:5.11.0-38-generic;  Version:#42~20.04.1-Ubuntu SMP Tue Sep 28 20:41:07 UTC 2021; Indentificator:x86_64
    INFO 2021-11-14 20:38:32,401 root : Ключ: client_info, Значення: Browser: python-requests/2.26.0  IP: 172.17.0.1 
    INFO 2021-11-14 20:39:32,450 root : Сервер доступний. Час на сервері: 14.11.21 20:39
    INFO 2021-11-14 20:39:32,450 root : Запитувана сторінка: : localhost:8000/health/
    INFO 2021-11-14 20:39:32,451 root : Відповідь сервера місти наступні поля:
    INFO 2021-11-14 20:39:32,451 root : Ключ: date, Значення: 14.11.21 20:39
    INFO 2021-11-14 20:39:32,451 root : Ключ: current_page, Значення: localhost:8000/health/
    INFO 2021-11-14 20:39:32,451 root : Ключ: server_info, Значення: OSName: Linux; NodeName: b5650a934aea; Release:5.11.0-38-generic;  Version:#42~20.04.1-Ubuntu SMP Tue Sep 28 20:41:07 UTC 2021; Indentificator:x86_64
    INFO 2021-11-14 20:39:32,451 root : Ключ: client_info, Значення: Browser: python-requests/2.26.0  IP: 172.17.0.1 
    INFO 2021-11-14 20:40:32,513 root : Сервер доступний. Час на сервері: 14.11.21 20:40
    INFO 2021-11-14 20:40:32,513 root : Запитувана сторінка: : localhost:8000/health/
    INFO 2021-11-14 20:40:32,513 root : Відповідь сервера місти наступні поля:
    INFO 2021-11-14 20:40:32,513 root : Ключ: date, Значення: 14.11.21 20:40
    INFO 2021-11-14 20:40:32,513 root : Ключ: current_page, Значення: localhost:8000/health/
    INFO 2021-11-14 20:40:32,513 root : Ключ: server_info, Значення: OSName: Linux; NodeName: b5650a934aea; Release:5.11.0-38-generic;  Version:#42~20.04.1-Ubuntu SMP Tue Sep 28 20:41:07 UTC 2021; Indentificator:x86_64
    INFO 2021-11-14 20:40:32,513 root : Ключ: client_info, Значення: Browser: python-requests/2.26.0  IP: 172.17.0.1 
    ```
4. ##### Закомітив `Dockerfile.site` та результати роботи програми моніторингу запущеної з `Docker` контейнера.

