# Выпускная квалификационная работа по теме OB2 - Платформа для публикации платного контента.
## Выполнил студент группы python 18.0 Салимгареев Адиль
_Это - сайт, на котором пользователи могут размещать свои мнения (посты) о чем угодно._
### Установка
> * Скопируйте репозиторий
> * Установите все зависимости
> * Заполните файл .env
> * Примените миграции (_python manage.py migrate_)
> * Загрузите данные для БД (_python manage.py loaddata data.json_)
> * Запустите проект (_python manage.py runserver_)
### Реализованные модели
> * Post - Мнение (пост), опубликованный на платформе любым пользователем
> * User - пользователь программы
### Роли пользователей
Пользователей можно условно разделить на несколько групп:
> 1. **Community** - индивиды, заплатившие за премиум на платформе
> 2. **Society** - пользователи без аккаунта
> 3. **Нечто среднее** - пользователи, создавшие аккаунт, но не заплатившие за премиум
### Роли постов
У постов есть 2 группы, которые отображаются на разных страницах:
> 1. **Community** - посты, опубликованные платными пользователями. На страницу с такими постами вас будет часто редиректить
> 2. **Society** - посты всех тех, кто не заплатил за премиум
### Права доступа
Каждый аутентифицированный пользователь может выполнять **любые действия со своими постами**. Посты анонимов может потрогать только админ
### Кастомные команды
У нас есть одна кастомная команда - _python manage.py create_users_. Используйте ее, если вам захочется пересоздать юзеров
### Тесты
Отчет прилагается (_report.txt_)
### Stripe
Реализована интеграция со Stripe. Чтобы начать пользоваться ею, вам необходимо заполнить некоторые поля в .env:
> * PRICE - строка из кучи букв и цифр, начинающаяся с _price_
> * STRIPE_API - ваш секретный API ключ. Начинается с _sk_test_ (дальше тестирования вы вряд-ли уйдете :) )
> * WEBHOOK_SECRET - ваш секретный WEBHOOK ключ. Вы можете создать его во вкладке endpoints, выбрав локальное тестирование. Начинается такой ключ с _whsec_

После заполнения всех полей, вы сможете принимать ~~тестовые~~ платежи
### Docker
Круть, у нас (вроде) работает Docker! Чтобы собрать и запустить контейнеры, введите команду _docker-compose up -d --build_ 
### P.S.
Не забудьте поменять значение для _POSTGRES_HOST_ в файле .env !