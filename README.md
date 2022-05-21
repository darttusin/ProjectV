# ProjectV - трекинг объектов при помощи DeepSort на модели нейронной сети YOLOv4 DarkNet
### Важно
#### Перед запуском проекта необходимо иметь версию OpenCV с поддержкой GStreamer
### Инструкция для запуска проекта на сервере:
- Клонируем git репозиторий с помрщью команды </br>
```
git clone https://github.com/darttusin/ProjectV
```
- Заходим в папку с репозиторием </br>
```
$ cd ProjectV
```
- Заносим в файл postgres.env все переменные окружения, необходимые для запуска PostgreSQL
Пример файла postgres.env:
```
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres'
PGADMIN_DEFAULT_EMAIL='pgadmin4@pgadmin.org'
PGADMIN_DEFAULT_PASSWORD='admin'
```
- Запускаем отдельно PGAdmin и PostgreSQL через docker-compose файл
```
docker-compose up --build --no-deps pgadmin postgres
```
- Переходим в PGAdmin по IP-адресу 
```
localhost:5050
```
 и создаем базу данных tracking_stats, а в ней с помощью SQL-Query саму таблицу
```
CREATE TABLE tracking_stats_table (
    trackerid INT NOT NULL,
    class TEXT NOT NULL,
    coordxmin INT NOT NULL,
    coordymin INT NOT NULL,
    coordxmax INT NOT NULL,
    coordymax INT NOT NULL
);
```
- Поднимаем все остальные контейнеры
```
docker-compose up --build
```
- После при вызове следующей команды
```
docker ps -a
```
- Вы должны увидеть список запущенных контейнеров
![alt text](https://sun9-43.userapi.com/s/v1/if2/kzkp5jX5YANBvcpWSlW4q-iorJD9_SgEJWcfCG83paW0lSiaOFOzJPyOSs88z3bCZilhTIcLvPg54uLvW-Uapxo8.jpg?size=1210x122&quality=96&type=album)

