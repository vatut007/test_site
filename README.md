# test_site
Репозиторий тествого задания Интер Мед

Установка проекта:

1. Клонировать репозиторий:
```
Git clone git@github.com:vatut007/test_site.git
```

2. Создать и активировать виртуальное окуружение:

```
python -m venv venv
```

Для linux:
```
source venv/bin/activate
```

Для windows:
```
source venv/scripts/activate
```

3. Обновить pip и установить зависимости из requirements.txt
```
python -m pip install --upgrade pip

pip install -r requirements.txt

```

4. Запустить проект 

```
python manage.py runserver

```

После запуска проект будет доступен по адресу: http://127.0.0.1:8000/init_db

Поиск принимает следующие параметры:

1) Фио пациента
2) Дата рождение (пример 2005-08-09)
3) Идентификатор исследования во внешней системе
4) Дата и время исследования (2023-03-10 12:24)
5) Модальность

Сортировка доступна при нажатии на колонки. Сортировка происходит в порядке возростания. При наличии параметра поиска, сортировка происходит по найденным данным.