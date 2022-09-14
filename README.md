
### Что делает?
- При нажатии в excel файле кнопку "Загрузить", запускается скрипт upload.exe и забирает данные с заполненными полями, занося их в БД Postgres

### Изображение
![image](https://user-images.githubusercontent.com/72396348/134735255-c71d9190-5b4b-4d9a-997a-3614d685c432.png)

### Описание задачи 1
<details>

Задача - Создать скрипт upload.py (python 3) и из него исполняемый файл upload.exe, запускаемый по кнопке "Загрузить"* в файле "названия точек.xlsm",
для загрузки/обновления данных из файла в таблицу в БД Postgres. 

*При нажатии кнопки, VBA макрос(уже есть в файле "названия точек.xlsm") запускает upload.exe с аргументом (путь до файла "названия точек.xlsm")

1. Создать таблицу endpoint_names в БД для загрузки данных
2. Написать скрипт загрузки данных upload.py
3. Создать из скрипта исполняемый файл upload.exe
4. Настроить макрос кнопки

Результат:
1. доработанный файл "названия точек.xlsm"
2. upload.py
3. upload.exe
  
</details>  
