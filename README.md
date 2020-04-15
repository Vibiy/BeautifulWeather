# BeautifulWeather
# Умный сервис прогноза погоды. Средний уровень сложности.

Сделано с использованием Python 3, Django.

Сайт состоит из одной страницы ("/"), на которой пользователь вводит название города, где он хочет узнать погоду, по английски. 
После отправки формы идет post запрос и создается объект заявки. Создание записи в БД сделано как заделка на будущее, чтобы не отправлять каждый раз запрос на сервис прогноза погоды и не расходовать понапрасну лимиты. 
TODO: Нужно будет добавить проверку, если за последние 10 минут уже был запрос для этого города - то просто выводить результат, полученный ранее (на сайте сервиса результаты как раз обновляются за такой период). 
В запросе на сервис указано получение результата в html. Этот ответ транслируется пользователю.
TODO: сменить тип результата и сделать красивый вывод данных.

# Для запуска 
нужно клонировать проект, составить .env файл (на уровне c manage.py):
```
SECRET_KEY=
DEBUG=True
HOST=0.0.0.0
DATABASE_NAME=beautiful_weather_db
DATABASE_USER=user
DATABASE_PASSWORD=password
WEATHER_API_KEY=
WEATHER_API_URL=http://api.openweathermap.org/data/2.5/weather
```
Создать локально БД PostgreSQL (и запустить сервер с постгрес если нет).
$ psql postgres
$ create database DATABASE_NAME with owner DATABASE_USER template template0 encoding 'utf8';
$ \q
Создать виртуальное окружение c Python 3. 
$ virtualenv --python=python3 env
Активировать его. 
$ source env/bin/activate
Перейти на уровень ниже
$ cd beautiful_weather/
Установить все из requirements.txt
$ pip install -r requirements.txt
Запустить проект
$ python manage.py runserver

Для проверки могу выслать свой env-файл.
TODO: завернуть в докер, чтобы было прилично. Пока очень сыро.

Видео: https://www.loom.com/share/c3b1e74c1c004133a46ac492d1172945
