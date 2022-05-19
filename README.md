# ProjectV - трекинг объектов с помощью дипсов на модели нейронной сети YOLOv4 darknet
### Инструкция для запуска проекта на сервере:
- Склонируете git репозиторий с помрщью команды </br>
```
git clone https://github.com/darttusin/ProjectV
```
- Скомпилируйте opencv с gstreamer </br>
```
# cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local  -D INSTALL_C_EXAMPLES=OFF  -D INSTALL_PYTHON_EXAMPLES=ON   -D BUILD_EXAMPLES=ON  -D PYTHON_EXECUTABLE=/usr/bin/python3  -D PYTHON_NUMPY_INCLUDE_DIRS=/usr/local/lib/python3.6/dist-packages/numpy/core/include/  -D WITH_GSTREAMER=ON -D WITH_GTK=ON  -D WITH_GTHREAD=ON -D WITH_TBB=ON   -DWITH_OPENGL=ON  ..
```
- Запускаем opencv с gstreamer через DOCKER COMPOSE

с подключенной папкой файловой системы Windows
```
winpty docker run -v //c/data:/home/data -p 5000:5000/udp -p 5004:5004/udp -it video_test.py 
```
при смонтированной папке файловой системы wsl
это происходит быстрее, так как docker и будет использовать одну и ту же файловую систему
```
winpty docker run -v //wsl$/Ubuntu-20.04/home/<user_name>/data:/home/data -it video_test.py 
```
  note: `winpty` is required when executing on windows from git-bash
  port 5000 is the videao stream
  port 5004 is mavlink
- Создание Базы данных tracking_stats </br>
После того, как мы подключились к серверу MySQL и запустили командную строку MySQL, время начать жизненный цикл нашей базы данных сайта, который стартует с её создания. Для создания базы данных MySQL через командную строку нужно ввести следующую команду:
```
CREATE DATABASE tracking_stats;
```
- Создание пользователя MySQL в командной строке
В командной строке MySQL это делается следующим образом:
```
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
```
- Создание таблицы </br>
```
CREATE TABLE tracking_stats_table (trackerid INT, class TEXT, coordxmin INT, coordymin INT,coordxmax INT,coordymax INT );
```


