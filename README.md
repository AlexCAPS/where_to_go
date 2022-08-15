# Where to go

Интерактивная карта Москвы, на которой могут быть отображены различные интересные локации и описание к ним.

Вы можете посетить раздел `/admin`, в котором вам предоставляется возможность управлять контентом, отображаемом на 
карте.

Ознакомьтесь с демо https://alexcaps.pythonanywhere.com/

В разделе Places вы можете создавать и редактировать отображаемые на карте локации, а также описание к ним. 
Также вы можете дополнить описание локации изображением или фото.


## Запуск проекта (локально)

### Окружение и зависимости
Для работы проекта необходим [интерпретатор Python](https://www.python.org/downloads/) версии 3.8 и выше.

Загрузите исходники проекта при помощи утилиты git или скачайте архив с исходниками проекта и распакуйте его в рабочем
каталоге.

Откройте командный интерпретатор и перейдите в корневой каталог проекта.

Рекомендуется создать [виртуальное окружение](https://docs.python.org/3/library/venv.html) и активировать его, чтобы 
устанавливаемые в следующих шагах зависимости не производили изменений в библиотеках операционной системы.

```shell
cd where_to_go/

virtualenv -p python3 venv

source venv/bin/activate
```

Установите зависимости проекта с помощью команды

```shell
pip install -r requirements.txt
```

Проверить корректность установки зависимостей вы можете просмотрев логи выполнения установки пакетов. Кроме того команда
`./manage.py --help`, при корректно установленных зависимостях, выведет на экран перечень доступных команд.


### Используемые переменные среды окружения

Могут быть отредактированы в файле `.env` следующие переменные среды окружения:

* [SECRET_KEY](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-SECRET_KEY)
* [DEBUG](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-DEBUG) 
* [ALLOWED_HOSTS](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-ALLOWED_HOSTS)
* [STATIC_URL](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-STATIC_URL)
* [STATIC_ROOT](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-STATIC_ROOT)
* [MEDIA_URL](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-MEDIA_URL)
* [MEDIA_ROOT](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-MEDIA_ROOT)

Пример

```dotenv
SECRET_KEY="Not secret key"
DEBUG=True
ALLOWED_HOSTS=
STATIC_URL='static/'
STATIC_ROOT="./static_files"
MEDIA_URL="media/"
MEDIA_ROOT="media/"
TOP_SLICE=1000
```


### Инициализация базы данных

Выполните следующую команду для создания базы данных и необходимых таблиц в ней

```shell
./manage.py migrate
```


### Создание первого пользователя

Для создания пользователя с правами администратора проекта необходимо выполнить следующую команду и в интерактивном 
режиме ввести запрашиваемые данные. Введение email может быть пропущено нажатием Enter.

```shell
./manage.py createsuperuser
```
Запомните вводимые имя пользователя и пароль. Они потребуются для доступа к разделу `/admin`.


### Запуск сервера

Для локального запуска сервера выполните команду 

```shell
./manage.py runserver
```

При успешном запуске в консоль будут выведены следующие сообщения с указанием URL для открытия стартовой страницы 
проекта.

```shell
Django version 4.0.5, using settings 'where_to_go.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

Вы можете изменить IP адрес и порт, используемые сервером, изменив команду запуска следующим образом:

```shell
./manage.py runserver 0.0.0.0:8080
```

### Импорт данных из json файлов

С помощью команды `load_place` вы можете произвести загрузку данных об интересных местах из json файлов, если их формат 
совпадает с форматом приведённого ниже примера.

```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

Загрузите архив с json файлами и распакуйте его в каталог (например, `/tmp/places`)

Выполните команду загрузки всех фалов из каталога:

```shell
find /tmp/places -name '*.json'  -exec ./manage.py load_place {} \;
```

Также вы можете произвести загрузку данных об интересном месте, если передадите команде `load_place` в качестве 
аргумента url json файла.

```shell
./manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json

```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
