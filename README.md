### Веб-сервис голосования

[Работа с GitHub](GitHub%20Workflow.md)  
[Техническое задание](Техническое%20задание.md)

### Как запустить backend:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/SUSU-Projects/votes.git
```

Перейти в папку с проектом

```
cd backend
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Создать администратора

```
python manage.py createsuperuser
```

Запустить проект:

```
python manage.py runserver
```

Документация доступна по [ссылке](http://127.0.0.1:8000/redoc/)
### Как запустить frontend:

Перед тем как начать, убедитесь, что у вас установлены следующие компоненты:

- Node.js и npm ([официальный сайт](https://nodejs.org/))

Перейти в папку frontend
```commandline
cd frontend
```

Установить зависимости из package.json командой
```commandline
npm install
```

Для запуска проекта сначала запустить сервер из папки backend в отдельном терминале командой

```
python manage.py runserver
```
затем открыть второй терминал, из папки frontend запустить React командой
```commandline
npm start
```