📸 Text Blog Project (English Version)
🌈 Description
Picture Blog Project is a custom-built blog designed for both personal use and collaboration with other users. The project supports PostgreSQL and features a REST API for external integrations. The frontend is primarily built with Bootstrap, ensuring a responsive and user-friendly interface.

🔥 The main idea of the project is to make blogging intuitive and content interaction as convenient as possible. Thanks to a flexible system of tags and categories, users can easily structure their content, while likes help highlight the most popular posts. This is a great tool for both personal use and creating a community of like-minded people.

🔧 Setup & Launch
1️⃣ Install dependencies
Make sure you have Python 3.x and PostgreSQL installed. Then, run:

bash
Копировать
Редактировать
pip install -r requirements.txt
2️⃣ Configure the database
Create a PostgreSQL database and update your settings.py file:

python
Копировать
Редактировать
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply migrations:

bash
Копировать
Редактировать
python manage.py migrate
3️⃣ Create a superuser
To access the admin panel, create a superuser:

bash
Копировать
Редактировать
python manage.py createsuperuser
Or use the default credentials:
📌 Username: admin
🔑 Password: admin

4️⃣ Run the server
bash
Копировать
Редактировать
python manage.py runserver
The server will be available at: http://127.0.0.1:8000

🌟 Key Features
✅ User registration & authentication
✅ Commenting system
✅ Post publishing with images
✅ REST API support
✅ Responsive UI (Bootstrap)
✅ PostgreSQL integration
✅ Django admin panel

🚀 Additional Features
You can deploy the project to a server using ngrok (if no dedicated hosting is available):

bash
Копировать
Редактировать
ngrok http 8000
Copy the generated address and add it to ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS in settings.py.

The project's API can be used for integrations with other services.

📩 Contact
If you have any questions or suggestions, feel free to reach out! 😎




📸 Text Blog Project (Українська версія)


🌈 Опис
Picture Blog Project — це власноруч створений блог, призначений для особистого використання або співпраці з іншими користувачами. Проєкт підтримує PostgreSQL та має REST API для взаємодії із зовнішніми сервісами. Клієнтська частина побудована на основі Bootstrap, що забезпечує адаптивний та зручний інтерфейс.

🔥 Основна ідея проєкту — зробити ведення блогу інтуїтивно зрозумілим, а взаємодію з контентом максимально зручною. Завдяки гнучкій системі тегів і категорій, користувачі можуть легко структурувати свій контент, а лайки допомагають знаходити найпопулярніші публікації. Це чудовий інструмент як для особистого використання, так і для створення спільнот за інтересами.

🔧 Налаштування та запуск
1️⃣ Встановлення залежностей
Переконайтеся, що у вас встановлені Python 3.x та PostgreSQL. Потім виконайте:

bash
Копировать
Редактировать
pip install -r requirements.txt
2️⃣ Налаштування бази даних
Створіть базу даних у PostgreSQL та оновіть файл settings.py:

python
Копировать
Редактировать
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Застосуйте міграції:

bash
Копировать
Редактировать
python manage.py migrate
3️⃣ Створення суперкористувача
Щоб увійти в адміністративну панель, створіть суперкористувача:

bash
Копировать
Редактировать
python manage.py createsuperuser
Або використовуйте стандартні дані:
📌 Логін: admin
🔑 Пароль: admin

4️⃣ Запуск сервера
bash
Копировать
Редактировать
python manage.py runserver
Сервер буде доступний за адресою: http://127.0.0.1:8000

🌟 Основні функції
✅ Реєстрація та автентифікація користувачів
✅ Система коментарів
✅ Публікація постів із зображеннями
✅ Підтримка REST API
✅ Адаптивний інтерфейс (Bootstrap)
✅ Підключення до PostgreSQL
✅ Адмін-панель Django

🚀 Додаткові можливості
Можна розгорнути проєкт на сервері за допомогою ngrok (якщо немає виділеного хостингу):

bash
Копировать
Редактировать
ngrok http 8000
Скопіюйте згенеровану адресу та додайте її в ALLOWED_HOSTS і CSRF_TRUSTED_ORIGINS у settings.py.

API проєкту можна використовувати для інтеграції з іншими сервісами.

📩 Контакти
Якщо у вас є питання або пропозиції, пишіть! 😎


# 📸 Text Blog Project (Русская версия)

## 🌈 Описание

**Picture Blog Project** — это самописный блог, созданный для ведения как лично, так и с другими пользователями. Проект поддерживает работу с **PostgreSQL**, а также имеет **REST API** для взаимодействия с внешними сервисами. Клиентская часть в основном построена с использованием **Bootstrap**, что делает интерфейс адаптивным и удобным.
🔥 Главная идея проекта — сделать ведение блога интуитивно понятным, а взаимодействие с контентом — максимально удобным. Благодаря гибкой системе тегов и разделов, пользователи могут легко структурировать свой контент, а лайки позволяют находить самые популярные публикации. Это отличный инструмент как для личного использования, так и для создания сообщества по интересам.


## 🔧 Настройка и запуск

### 1️⃣ Установка зависимостей
Перед запуском проекта убедитесь, что у вас установлен **Python 3.x** и **PostgreSQL**. Затем выполните:
bash
pip install -r requirements.txt


### 2️⃣ Настройка базы данных
Создайте базу данных в **PostgreSQL**, затем настройте подключение в settings.py:
python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Примените миграции:
bash
python manage.py migrate


### 3️⃣ Создание суперпользователя
Для входа в административную панель создайте суперпользователя:
bash
python manage.py createsuperuser


**Либо используйте стандартные данные:**  
📌 **Логин:** admin  
🔑 **Пароль:** admin

### 4️⃣ Запуск сервера
bash
python manage.py runserver

После запуска сервер будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🌟 Основные функции

✅ **Регистрация и аутентификация пользователей**  
✅ **Система коментарие**
✅ **Публикация записей с изображениями**  
✅ **Поддержка REST API**  
✅ **Адаптивный интерфейс (Bootstrap)**  
✅ **Подключение к PostgreSQL**  
✅ **Панель администратора Django**  

## 🚀 Дополнительные возможности

- Можно развернуть проект на **сервере** с помощью **ngrok** (если нет выделенного хостинга):
  
bash
  ngrok http 8000

  Скопируйте сгенерированный адрес и добавьте его в ALLOWED_HOSTS и CSRF_TRUSTED_ORIGINS в settings.py.

- API проекта можно использовать для интеграции с другими сервисами.

## 📩 Контакты
Если у вас есть вопросы или предложения, пишите! 😎


Напиши еще две версии на англ и на украинском

