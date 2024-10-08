# YourOpinion
### _Платформа, на котором пользователи могут размещать свои мнения (посты) о чем угодно._
### Установка
> * Скопируйте репозиторий
> * Установите все зависимости
> * Заполните файл .env
> * Примените миграции (_python manage.py migrate_)
> * Загрузите тестовые данные для БД (_python manage.py loaddata data.json_)
### Реализованные модели
> * Post - Объявление/пост, опубликованный на платформе любым пользователем
> * User - пользователь платформы
### Роли пользователей
Пользователей можно условно разделить на несколько групп:
> 1. **Community** - премиум-пользователи
> 2. **Society** - пользователи без аккаунта
> 3. **Community с флагом is_paid=False** - пользователи, с созданным аккаунтом
### Роли постов
У постов есть 2 группы, которые отображаются на разных страницах:
> 1. **Community** - посты, опубликованные премиум-пользователями.
> 2. **Society** - все остальные посты
### Права доступа
Каждый аутентифицированный пользователь может выполнять **любые действия со своими постами**. Посты анонимных пользователей может изменять только админ
### Кастомные команды
_python manage.py create_users_ - Используйте ее, если вам захочется пересоздать тестовых юзеров
### Stripe
Реализована интеграция со Stripe. Чтобы начать пользоваться ею, вам необходимо заполнить некоторые поля в .env:
> * PRICE - ценник.
> * STRIPE_API - ваш секретный API ключ.
> * WEBHOOK_SECRET - ваш секретный WEBHOOK ключ.
### P.S.
Не забудьте поменять значение для _POSTGRES_HOST_ в файле .env !